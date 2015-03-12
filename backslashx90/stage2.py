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

from function_comb import FnName

#Perform Register Selection
def selection(ast, fn):
    st2 = Stage2();
    return st2.assemble(ast, fn);

#The Register Selection Object
class Stage2:
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

#Create the Asm tree and then Allocate Registers
    def assemble(self, ast, fn):
        self.instructionSelection(ast, fn);
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
        

#Select Instructions
    def instructionSelection(self, lst, fn):
        for ast in lst:
            if isinstance(ast, core.Comment):
                self.addAsm( Comment(ast.comment) )
            elif isinstance(ast, core.Assign):
                self.addAsm( Comment("End Instruction \n\n")) 
                self.addAsm( Comment("*" + str(ast)) )
                name = ast.name
                op = ast.rhs
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
                    self.addAsm( Call("get_subscript") )
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


            elif isinstance(ast, core.If):
                cond = ast.cond
                thens = ast.then_stmts
                elses = ast.else_stmts

                
                tmpv = var_spill(self.tmpvar())

                self.addAsm( Movl(self.to_base_asm(cond), tmpv) )
                self.addAsm( Testl(tmpv, tmpv) )

                old_asm = self.AsmTree
                self.AsmTree = []

                self.instructionSelection(thens, fn)
                new_thens = self.AsmTree
                self.AsmTree = []

                self.instructionSelection(elses, fn)
                new_elses = self.AsmTree

                self.AsmTree = old_asm

                self.addAsm( If( NOT_ZERO, new_thens, new_elses ) )



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

            raise Exception("Unexpected %s in assemble" % ast.__class__)

