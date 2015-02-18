# Create the Asm Tree and then do register selection 
#
#
from viper.register_selector import allocate_registers
from viper.AsmTree import Movl, Addl, Neg, Push,  Call, Subl
import viper.core as core
from viper.AsmTypes import SPILL, CALLER_SAVED, RAW, CONSTANT, AsmVar

#Perform Register Selection
def selection(ast):
    st2 = Stage2();
    return st2.assemble(ast);

#The Register Selection Object
class Stage2:
    def __init__(self):
        self.namenum = 0
        self.nametrans = {}
        self.AsmTree = []

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
    def to_base_asm( self, ast ): # -> AsmVar
        if isinstance(ast, core.Const):
            return AsmVar(ast.raw, CONSTANT)
        elif isinstance(ast, core.Name):
            if( isinstance(ast.name, int) ):
                return AsmVar(str(ast.name), CONSTANT)
            return AsmVar(ast.name)
        raise WTFException()

#Select Instructions
    def instructionSelection(self, lst):
        for ast in lst:
            if isinstance(ast, core.Assign):
                name = ast.name
                op = ast.rhs
                if isinstance(op, core.Add):
                    self.AsmTree.append(Movl(self.to_base_asm(op.lhs), AsmVar(name)))
                    self.AsmTree.append(Addl(self.to_base_asm(op.rhs), AsmVar(name)))

                if isinstance(op, core.Neg):
                    self.AsmTree.append(Movl(self.to_base_asm(op.rhs), AsmVar( name )))
                    self.AsmTree.append(Neg(AsmVar( name )))

                elif isinstance(op, core.Const):
                    self.AsmTree.append(Movl(self.to_base_asm(op), AsmVar( name ) ))
                
                elif isinstance(op, core.Name):
                    self.AsmTree.append(Movl(self.to_base_asm(op), AsmVar( name )))

                elif isinstance(op, core.CallFunc):
                    self.AsmTree.append(Subl(AsmVar("12", CONSTANT), AsmVar("%esp", RAW)))
                    self.AsmTree.append(Movl(AsmVar("%eax", RAW), AsmVar("(%esp)" , RAW)))
                    self.AsmTree.append(Movl(AsmVar("%ecx", RAW), AsmVar("4(%esp)", RAW)))
                    self.AsmTree.append(Movl(AsmVar("%edx", RAW), AsmVar("8(%esp)", RAW)))

                    self.AsmTree.append(Call(self.to_base_asm(op.lhs)))
                    self.AsmTree.append(Movl(AsmVar("%eax", RAW), AsmVar(name)))

                    self.AsmTree.append(Movl(AsmVar("(%esp)", RAW), AsmVar("%eax", RAW)))
                    self.AsmTree.append(Movl(AsmVar("4(%esp)", RAW),AsmVar("%ecx", RAW)))
                    self.AsmTree.append(Movl(AsmVar("8(%esp)", RAW),AsmVar("%edx", RAW)))
                    self.AsmTree.append(Addl(AsmVar("12", CONSTANT),AsmVar("%esp", RAW)))

            elif isinstance(ast, core.Print):
                self.AsmTree.append(Subl(
                    AsmVar("12", CONSTANT), AsmVar("%esp", RAW)))
                self.AsmTree.append(Movl(
                    AsmVar("%eax", RAW), AsmVar("(%esp)", RAW) ))
                self.AsmTree.append(Movl(
                    AsmVar("%ecx", RAW), AsmVar("4(%esp)", RAW)))
                self.AsmTree.append(Movl(
                    AsmVar("%edx", RAW), AsmVar("8(%esp)", RAW)))
                self.AsmTree.append(Push(self.to_base_asm(ast.rhs)))
                # self.AsmTree.append(Movl(self.to_base_asm(ast.rhs), '%(%esp)'))
                self.AsmTree.append(Call(AsmVar("print_int_nl", RAW))) 
                self.AsmTree.append(Movl(
                    AsmVar("4(%esp)", RAW), AsmVar("%eax", RAW)))

                self.AsmTree.append(Movl(
                    AsmVar("8(%esp)", RAW), AsmVar("%ecx", RAW)))
                self.AsmTree.append(Movl(
                    AsmVar("12(%esp)", RAW), AsmVar("%edx", RAW)))
                self.AsmTree.append(Addl(
                    AsmVar("16", CONSTANT), AsmVar("%esp", RAW)))

