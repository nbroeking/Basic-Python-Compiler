# Create the Asm Tree and then do register selection 
#
#
from viper.register_selector import allocate_registers
from viper.AsmTree import *
import viper.core as core
from viper.AsmTypes import *

#Perform Register Selection
def selection(ast):
    st2 = Stage2();
    return st2.assemble(ast);

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
    def assemble(self, ast):
        self.instructionSelection(ast);
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
    def instructionSelection(self, lst):
        for ast in lst:
            if isinstance(ast, core.Assign):
                name = ast.name
                op = ast.rhs
                print "TEST: %s %s" % (name.__class__, op.__class__)
                if isinstance(op, core.List):
                    self.save_registers()

                    self.addAsm( Subl( var_const("4"), var_raw("%esp") ) )
                    self.addAsm( Movl( var_const(str(len(op.elems))), var_raw_mem("(%esp)") ) )
                    self.addAsm( Call("create_list") )
                    self.addAsm( Movl( var_raw("%eax"), var_caller_saved(name) ) )
                    self.addAsm( Addl( var_const("4"), var_raw("%esp") ) )
                    self.restore_registers()

                    # ugly hack
                    self.addAsm( Push( var_raw("%eax") ) )
                    self.addAsm( Movl( var_caller_saved(name), var_raw("%eax") ))
                    self.addAsm( Movl( var_raw("4(%eax)"), var_raw("%eax") ) )

                    i = 0
                    for elem in op.elems:
                        self.addAsm( Movl( self.to_base_asm(elem, CALLER_SAVED), var_raw_mem("0x%x(%%eax)" % i) ) )
                        i += 4

                    self.addAsm( Pop( var_raw("%eax") ))

                elif isinstance(op, core.Deref):
                    self.AsmTree.append(Movl(AsmVar(op.arg, 0, op.offset), AsmVar(name)))
                    
                elif isinstance(op, core.PyAdd):
                    v = self.tmpvar()
                    vname = var_caller_saved(name)
                    self.addAsm(Movl(self.to_base_asm(op.lhs), vname))
                    self.addAsm(Movl(self.to_base_asm(op.rhs), AsmVar(v)))

                    self.addAsm(Andl(var_const("3"), AsmVar(v)))
                    self.addAsm(Andl(var_const("3"), vname))
                    
                    labnr = self.newlabelnr()
                    self.addAsm(Cmpl(AsmVar(v), vname))
                    self.addAsm(Jnz("puke"))
                    self.addAsm(Testl(AsmVar(v), AsmVar(v)))

                    self.addAsm(If( ZERO, [
                          Movl(self.to_base_asm(op.lhs), vname)
                        , Addl(self.to_base_asm(op.rhs), vname)
                        ],
                        self.save_registers_arr(20) + [
                          Movl(self.to_base_asm(op.lhs), var_raw_mem("(%esp)"))
                        , Movl(self.to_base_asm(op.rhs), var_raw_mem("4(%esp)"))
                        , Andl(var_const("0xFFFFFFFC"), var_raw_mem("(%esp)"))
                        , Andl(var_const("0xFFFFFFFC"), var_raw_mem("4(%esp)"))
                        , Call("add")
                        , Addl(var_const("3"), var_raw("%eax"))
                        , Movl(var_raw("%eax"), vname) ] +
                        self.restore_registers_arr(20)
                    ))

                    
                elif isinstance(op, core.Add):
                    self.AsmTree.append(Movl(self.to_base_asm(op.lhs), AsmVar(name)))
                    self.AsmTree.append(Addl(self.to_base_asm(op.rhs), AsmVar(name)))

                elif isinstance(op, core.Neg):
                    self.AsmTree.append(Movl(self.to_base_asm(op.rhs), AsmVar( name )))
                    self.AsmTree.append(Neg(AsmVar( name )))

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
                    self.AsmTree.append(Movl(AsmVar("%eax", RAW), AsmVar(name, CALLER_SAVED))) #NOTE:This variable was marked as * 
                    self.restore_registers(n_bytes)


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

