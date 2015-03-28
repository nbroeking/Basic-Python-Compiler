# Create the Asm Tree and then do register selection 
#
#

try:
    from viper.register_selector import allocate_registers
    from viper.AsmTree import *
    import viper.core as core
    from viper.AsmTypes import *

except:
    from register_selector import allocate_registers
    from AsmTree import *
    import core as core
    from AsmTypes import *

from function_comb import FnName, mangle

#Perform Register Selection
def selection(ast, defs, fname):
    st2 = Stage2();
    lst = st2.assemble(ast, defs, fname);
    return (st2.data_section, lst)

#The Register Selection Object
class Stage2:
    data_nonce = 0
    data_section = {}
    current_strings = set()

    def __init__(self):
        self.namenum = 0
        self.labelnum = 0
        self.nametrans = {}
        self.AsmTree = []
    
    def tmpvar(self):
        ret = "$s2_%d" % self.namenum
        self.namenum += 1
        return ret

    def newlabelnr(self):
        ret = self.labelnum
        self.labelnum += 1
        return ret

    def create_string(self, string):
        if not string in Stage2.data_section:
            name = ".str_%d" % Stage2.data_nonce
            Stage2.data_nonce += 1
            Stage2.data_section[string] = name
        else:
            name = Stage2.data_section[string]
        return name

#Create the Asm tree and then Allocate Registers
    def assemble(self, ast, defs, fname):
        self.instructionSelection(ast, defs, fname);
        print "-------- ASM TREE BEFORE REG"
        for i in self.AsmTree:
            print ("%s" % i._to_str())
        print "-------"
        print "\n"
        return allocate_registers(self.AsmTree)

#Convert base to AsmVar
    def to_base_asm( self, ast, flags=0 ): # -> AsmVar
        if isinstance(ast, core.Const):
            return AsmVar(str(ast.raw), CONSTANT)
        elif isinstance(ast, core.Name):
            if( isinstance(ast.name, int) ):
                return AsmVar(str(ast.name), CONSTANT)
            return AsmVar(str(ast.name), flags)
        print "Unexpected type %s" % ast.__class__
        raise WTFException()

    def addAsm(self, x):
        self.AsmTree.append(x)

    def save_registers_arr( self, amt=12 ):
        return [   Subl( var_const(str(amt)), var_raw("%esp"))
                 , Movl( var_raw("%eax"), var_raw_mem("0x%x(%%esp)" % (amt-12)))
                 , Movl( var_raw("%ecx"), var_raw_mem("0x%x(%%esp)" % (amt- 8)))
                 , Movl( var_raw("%edx"), var_raw_mem("0x%x(%%esp)" % (amt- 4))) ]

    def restore_registers_arr( self, amt=12 ):
        return [ Movl( var_raw_mem("0x%x(%%esp)" % (amt-12)), var_raw("%eax") )
               , Movl( var_raw_mem("0x%x(%%esp)" % (amt- 8)), var_raw("%ecx") )
               , Movl( var_raw_mem("0x%x(%%esp)" % (amt- 4)), var_raw("%edx") )
               , Addl( var_const(str(amt)), var_raw("%esp")) ]

    def save_registers( self, amt=12 ):
        map( self.addAsm, self.save_registers_arr(amt) )

    def restore_registers( self, amt=12 ):
        map( self.addAsm, self.restore_registers_arr(amt) )

    def set_subscript(self, lst_var, idx_var, val_var):
        self.save_registers(24)
        self.addAsm( Movl(lst_var, var_raw_mem("(%esp)")) )
        self.addAsm( Movl(idx_var, var_raw_mem("4(%esp)")) )
        self.addAsm( Movl(val_var, var_raw_mem("8(%esp)")) )
        self.addAsm( Call("set_subscript2") )
        self.restore_registers(24)

    def comment(self, cmt):
        self.addAsm(Comment(cmt))
        
    def update_closure(self, defined_function, variable_name):
        me = defined_function
        my_closure_dict = me.my_closure

        if variable_name in my_closure_dict:
            self.comment("Updating closure (%s) {{{" % variable_name)
            offset = my_closure_dict[variable_name]
            val_var = AsmVar(variable_name) 
            self.addAsm( Movl(val_var, AsmVar("$fn_closure", 0, offset*4)) )
            self.comment("}}}")
        
#Select Instructions
    def instructionSelection(self, lst, defs, fname, preamble=True):
        myfunction = defs[fname]
        myclosure = var_caller_saved("$fn_closure") # the closure for _this_ function
        
        if preamble:
            # First, move the value of the parent closure into the current scope
            i = 8
            myenv_n = self.tmpvar()
            self.addAsm( Comment("Bringing parent closure into local scope {{{") )
            self.addAsm(Movl(var_raw_mem("%s(%%ebp)" % (len(myfunction.args) * 4 + 8)), AsmVar(myenv_n)))
    
            # v: index into closure
            # k: name of variable
            for (k, v) in myfunction.parent_closure.items():
                self.addAsm( Movl( AsmVar(myenv_n, 0, v*4), AsmVar(k) ) )

            self.addAsm( Comment("}}}") )
    
            self.addAsm( Comment("Bringing arguments into local scope {{{") )
            for arg in myfunction.args:
                self.addAsm( Movl(var_raw_mem("%s(%%ebp)" % i), AsmVar(arg)) )
                i += 4
            self.addAsm( Comment("}}}") )

            self.addAsm( Comment("Building local closure {{{") )
            closure_size = len(myfunction.my_closure.items())
            self.save_registers(16)
            self.addAsm( Movl(var_const(str(closure_size*4)), var_raw_mem("(%esp)")) )
            # use a list for simplicity my ass
            # to hell with using a list! void* FTW!
            self.addAsm( Call("malloc") )
            self.addAsm( Movl(EAX, myclosure) )
            self.restore_registers(16)
            for k in myfunction.parent_closure.keys():
                self.update_closure(myfunction, k)
            for k in myfunction.args:
                self.update_closure(myfunction, k)
            self.addAsm( Comment("}}}") )

        for ast in lst:
            if isinstance(ast, core.Comment):
                self.addAsm( Comment(ast.comment) )
            elif isinstance(ast, core.Assign):
                self.addAsm( Comment("End Instruction \n\n")) 
                self.addAsm( Comment("*" + str(ast)) )
                name = ast.name # the name of the varialbe
                op = ast.rhs

                # {{{
                if isinstance(op, core.Deref):
                    self.AsmTree.append(Movl(AsmVar(op.arg, 0, op.offset), AsmVar(name)))
                    
                elif isinstance(op, core.PyAdd):
                    v = self.tmpvar()
                    vname = var_caller_saved(name)
                    self.addAsm(Movl(self.to_base_asm(op.lhs), vname))
                    self.addAsm(Movl(self.to_base_asm(op.rhs), AsmVar(v)))

                    # Will break with floats
                    self.addAsm(Andl(var_const("2"), AsmVar(v)))
                    self.addAsm(Andl(var_const("2"), vname))
                    
                    labnr = self.newlabelnr()
                    self.addAsm(Cmpl(AsmVar(v), vname))
                    self.addAsm(Jmp("puke", "jnz"))
                    self.addAsm(Testl(AsmVar(v), AsmVar(v)))

                    self.addAsm(If( ZERO, [
                          Movl(self.to_base_asm(op.lhs), vname)
                        , Addl(self.to_base_asm(op.rhs), vname)
                        , Andl(var_const("0xFFFFFFFC"), vname)
                        ],
                        self.save_registers_arr(20) + [
                          Movl(self.to_base_asm(op.lhs), var_raw_mem("(%esp)"))
                        , Movl(self.to_base_asm(op.rhs), var_raw_mem("4(%esp)"))
                        , Andl(var_const("0xFFFFFFFC"), var_raw_mem("(%esp)"))
                        , Andl(var_const("0xFFFFFFFC"), var_raw_mem("4(%esp)"))
                        , Call("add")
                        , Orl(var_const("3"), var_raw("%eax"))
                        , Movl(var_raw("%eax"), vname) ] +
                        self.restore_registers_arr(20)
                    ))

                elif isinstance(op, core.MakeClosure):
                    fn_name = op.name 
                    vname = var_caller_saved(name)

                    self.save_registers(28)
                    self.addAsm( Movl(var_const(fn_name), var_raw_mem("(%esp)")) )
                    self.addAsm( Movl(myclosure, var_raw_mem("4(%esp)")) )
                    self.addAsm( Call("create_closure") )
                    self.addAsm( Orl(var_const("3"), var_raw("%eax")) )
                    self.addAsm( Movl(var_raw("%eax"), vname) )
                    self.restore_registers(28)
                
                elif isinstance(op, core.Not):
                    vname = var_caller_saved(name)
                    self.save_registers(16)
                    self.addAsm( Movl(self.to_base_asm(op.rhs), var_raw_mem("(%esp)")) )
                    self.addAsm( Call("is_true") )
                    self.addAsm( Xorl(var_const("1"), var_raw("%eax")) )
                    self.addAsm( Shll( var_const("2"), var_raw("%eax") ))
                    self.addAsm( Orl( var_const("1"), var_raw("%eax") ))
                    self.addAsm( Movl(var_raw("%eax"), vname) )
                    self.restore_registers(16)
                
                elif isinstance(op, core.Equals):
                    v = self.tmpvar()
                    vname = var_caller_saved(name)
                    vname.setCantSpill()
                    self.addAsm(Movl(self.to_base_asm(op.lhs), vname))
                    self.addAsm(Movl(self.to_base_asm(op.rhs), AsmVar(v)))

                    # Will break with floats
                    self.addAsm(Andl(var_const("2"), AsmVar(v)))
                    self.addAsm(Andl(var_const("2"), vname))
                    
                    labnr = self.newlabelnr()
                    self.addAsm(Cmpl(AsmVar(v), vname))

                    t1 = AsmVar(self.tmpvar())
                    t2 = AsmVar(self.tmpvar())
                    t3 = AsmVar(self.tmpvar())

                    self.addAsm(If( NOT_ZERO, [ Movl(var_const("1"), vname) ],
                        [
                          Testl(AsmVar(v), AsmVar(v)),
                          If( ZERO, [
                            # is int or bool
                              Movl(self.to_base_asm(op.lhs), t1)
                            , Movl(self.to_base_asm(op.rhs), t2)
                            , Shrl(var_const("2"), t1)
                            , Shrl(var_const("2"), t2)
                            , Movl(var_const("5"), t3)
                            , Movl(var_const("1"), vname)
                            , Cmpl(t1, t2)
                            , Cmovzl(t3, vname)
                          ],
                            # is big obj
                            self.save_registers_arr(20) + [
                              Movl(self.to_base_asm(op.lhs), var_raw_mem("(%esp)"))
                            , Movl(self.to_base_asm(op.rhs), var_raw_mem("4(%esp)"))
                            , Andl(var_const("0xFFFFFFFC"), var_raw_mem("(%esp)"))
                            , Andl(var_const("0xFFFFFFFC"), var_raw_mem("4(%esp)"))
                            , Call("equal")
                            , Shll(var_const("2"), var_raw("%eax"))
                            , Orl(var_const("1"), var_raw("%eax"))
                            , Movl(var_raw("%eax"), vname) ] +
                            self.restore_registers_arr(20)
                          )

                        ] ))

                elif isinstance(op, core.AllocClass):
                    parent_list = var_caller_saved(self.tmpvar())
                    vname = var_caller_saved(name)
                    self.save_registers(16)
                    # TODO does not support inheritence
                    self.addAsm(Movl(var_const("0"), var_raw_mem("(%esp)")))
                    self.addAsm(Call("create_list"));
                    self.addAsm(Addl(var_const("3"), var_raw("%eax")))
                    self.addAsm(Movl(var_raw("%eax"), parent_list))
                    self.restore_registers(16)

                    self.save_registers(16)
                    self.addAsm(Movl(parent_list, var_raw_mem("(%esp)")))
                    self.addAsm(Call("create_class"))
                    self.addAsm(Addl(var_const("3"), var_raw("%eax")))
                    self.addAsm(Movl(var_raw("%eax"), vname))
                    self.restore_registers(16)

                elif isinstance(op, core.GetAttr):
                    vname = var_caller_saved(name)
                    strptr = self.create_string(op.attr)
                    self.save_registers(20)
                    self.addAsm(Movl(self.to_base_asm(op.lhs), var_raw_mem("(%esp)")))
                    self.addAsm(Movl(var_const(strptr), var_raw_mem("4(%esp)")))
                    self.addAsm(Call("get_attr"))
                    self.addAsm(Movl(var_raw("%eax"), vname))
                    self.restore_registers(20)

                elif isinstance(op, core.Is):
                    vname = var_spill(name)
                    t1 = AsmVar(self.tmpvar())
                    t2 = AsmVar(self.tmpvar())
                    t3 = AsmVar(self.tmpvar())

                    self.addAsm(Movl(self.to_base_asm(op.lhs), t1))
                    self.addAsm(Movl(self.to_base_asm(op.rhs), t2))
                    self.addAsm(Movl(var_const("1"), t3))
                    self.addAsm(Movl(var_raw("$0"), vname))

                    self.addAsm(Cmpl(t1, t2))
                    self.addAsm(Cmovzl(t3, vname))
                    self.addAsm(Shll(var_const("2"), vname))
                    self.addAsm(Orl(var_const("1"), vname))
                    
                elif isinstance(op, core.Subscript):
                    vname = var_caller_saved(name)
                    lhs = op.lhs
                    rhs = op.rhs
                    self.save_registers(20)
                    self.addAsm( Movl(self.to_base_asm(lhs), var_raw_mem("(%esp)")) )
                    self.addAsm( Movl(self.to_base_asm(rhs), var_raw_mem("4(%esp)")) )
                    self.addAsm( Call("get_subscript2") )
                    self.addAsm( Movl(var_raw("%eax"), vname) )
                    self.restore_registers(20)
                    
                elif isinstance(op, core.Add):
                    self.AsmTree.append(Movl(self.to_base_asm(op.lhs), AsmVar(name)))
                    self.AsmTree.append(Addl(self.to_base_asm(op.rhs), AsmVar(name)))

                elif isinstance(op, core.Return):
                    rhs = op.rhs
                    self.AsmTree.append(Movl(self.to_base_asm(rhs), var_raw("%eax")))
                    self.AsmTree.append(Jmp(".%s_ret", fn.name))

                elif isinstance(op, core.Neg):
                    self.AsmTree.append(Movl(self.to_base_asm(op.rhs), AsmVar( name )))
                    self.AsmTree.append(Shrl(var_const("2"), AsmVar(name)))
                    self.AsmTree.append(Neg(AsmVar( name )))
                    self.AsmTree.append(Shll(var_const("2"), AsmVar(name)))

                elif isinstance(op, core.Const):
                    self.AsmTree.append(Movl(self.to_base_asm(op), AsmVar( name ) ))
                
                elif isinstance(op, core.Name):
                    self.AsmTree.append(Movl(self.to_base_asm(op), AsmVar( name )))

                elif isinstance(op, core.CallFunc):
                    args = op.args
                    n_bytes = 12 + (len(args) << 2)

                    self.save_registers(n_bytes);

                    idx = 0
                    for i in args:
                        self.AsmTree.append( Movl(self.to_base_asm(i), var_raw_mem("0x%x(%%esp)" % idx)) )
                        idx += 4

                    self.AsmTree.append(Call(self.to_base_asm(op.lhs)))
                    self.AsmTree.append(Movl(AsmVar("%eax", RAW), AsmVar(name, CALLER_SAVED)))
                    self.restore_registers(n_bytes)

                elif isinstance(op, core.CallClosure):
                    args = op.args
                    n_bytes = 16 + (len(args) << 2)

                    self.save_registers(n_bytes);

                    idx = 0
                    for i in args:
                        self.AsmTree.append( Movl(self.to_base_asm(i), var_raw_mem("0x%x(%%esp)" % idx)) )
                        idx += 4

                    tmpname = self.tmpvar()
                    self.addAsm( Movl(AsmVar(op.lhs.name), AsmVar(tmpname)) )
                    self.addAsm( Andl(var_const("0xFFFFFFFC"), AsmVar(tmpname)) )
                    self.AsmTree.append( Movl(AsmVar(tmpname, 0, 8), var_raw_mem("0x%x(%%esp)" % idx)) )
                    self.AsmTree.append(CallStar(AsmVar(tmpname, 0, 4)))
                    self.AsmTree.append(Movl(AsmVar("%eax", RAW), AsmVar(name, CALLER_SAVED)))
                    self.restore_registers(n_bytes)

                # }}}

                self.update_closure(myfunction, name)

            elif isinstance(ast, core.SetAttr):
                op = ast
                strptr = self.create_string(op.attr)
                self.save_registers(24)
                self.addAsm(Movl(self.to_base_asm(op.lhs), var_raw_mem("(%esp)")))
                self.addAsm(Movl(var_const(strptr), var_raw_mem("4(%esp)")))
                self.addAsm(Movl(self.to_base_asm(op.rhs), var_raw_mem("8(%esp)")))
                self.addAsm(Call("set_attr"))
                self.restore_registers(24)
                
            elif isinstance(ast, core.If):
                cond = ast.cond
                thens = ast.then_stmts
                elses = ast.else_stmts

                
                tmpv = var_spill(self.tmpvar())

                self.addAsm( Movl(self.to_base_asm(cond), tmpv) )
                self.addAsm( Testl(tmpv, tmpv) )

                old_asm = self.AsmTree
                self.AsmTree = []

                self.instructionSelection(thens, defs, fname, False)
                new_thens = self.AsmTree
                self.AsmTree = []

                self.instructionSelection(elses, defs, fname, False)
                new_elses = self.AsmTree

                self.AsmTree = old_asm

                self.addAsm( If( NOT_ZERO, new_thens, new_elses ) )

            elif isinstance(ast, core.Return):
                self.addAsm( Movl(self.to_base_asm(ast.val), var_raw("%eax")) )
                self.addAsm( Jmp(".%s_ret" % fname) )


            elif isinstance(ast, core.Print):
                self.AsmTree.append(Subl(
                    AsmVar("12", CONSTANT), var_raw("%esp")))
                self.AsmTree.append(Movl(
                    AsmVar("%eax", RAW), var_raw_mem("(%esp)" )))
                self.AsmTree.append(Movl(
                    AsmVar("%ecx", RAW), var_raw_mem("4(%esp)")))
                self.AsmTree.append(Movl(
                    AsmVar("%edx", RAW), var_raw_mem("8(%esp)")))
                self.AsmTree.append(Push(self.to_base_asm(ast.rhs)))
                # self.AsmTree.append(Movl(self.to_base_asm(ast.rhs), '%(%esp)'))
                self.AsmTree.append(Call(AsmVar("print_any", RAW))) 
                self.AsmTree.append(Movl(
                    var_raw_mem("4(%esp)"), AsmVar("%eax", RAW)))

                self.AsmTree.append(Movl(
                    var_raw_mem("8(%esp)"), AsmVar("%ecx", RAW)))
                self.AsmTree.append(Movl(
                    var_raw_mem("12(%esp)"), AsmVar("%edx", RAW)))
                self.AsmTree.append(Addl(
                    AsmVar("16", CONSTANT), AsmVar("%esp", RAW)))

            else:
                raise Exception("Unexpected %s in assemble" % ast.__class__)

