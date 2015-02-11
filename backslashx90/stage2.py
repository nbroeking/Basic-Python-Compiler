# 
#

from register_selector import allocate_registers
from AsmTree import Movl, Addl, Neg, Push, Pop, Call, Subl
import core
import platform

def stage2(ast):
    st2 = Stage2();
    return st2.assemble(ast);


class Stage2:
    def __init__(self):
        self.namenum = 0
        self.nametrans = {}
        self.AsmTree = []


    def assemble(self, ast):
        self.instructionSelection(ast);
        print "----------------"
        for i in self.AsmTree:
            print ("%s" % i._to_str())
        print "----------------"
        return allocate_registers(self.AsmTree)

    def to_base_asm( self, ast ):
        if isinstance(ast, core.Const):
            return "&%s" % (ast.raw,) 
        elif isinstance(ast, core.Name):
            if( isinstance(ast.name, int) ):
                return ast.name
            return ast.name
        raise WTFException()

    def instructionSelection(self, lst):
        for ast in lst:
            if isinstance(ast, core.Assign):
                name = ast.name
                op = ast.rhs
                if isinstance(op, core.Add):
                    self.AsmTree.append(Movl(self.to_base_asm(op.lhs), name))
                    self.AsmTree.append(Addl(self.to_base_asm(op.rhs), name))

                if isinstance(op, core.Neg):
                    self.AsmTree.append(Movl(self.to_base_asm(op.rhs), name))
                    self.AsmTree.append(Neg(name))

                elif isinstance(op, core.Const):
                    self.AsmTree.append(Movl(self.to_base_asm(op), name ))
                
                elif isinstance(op, core.Name):
                    self.AsmTree.append(Movl(self.to_base_asm(op), name))

                elif isinstance(op, core.CallFunc):
                    self.AsmTree.append(Subl("&12", "%%esp"))
                    self.AsmTree.append(Movl("%%eax", "%(%esp)"))
                    self.AsmTree.append(Movl("%%ecx", "%4(%esp)"))
                    self.AsmTree.append(Movl("%%edx", "%8(%esp)"))

                    self.AsmTree.append(Call(self.to_base_asm(op.lhs)))
                    self.AsmTree.append(Movl("%%eax", name))

                    self.AsmTree.append(Movl("%(%esp)", "%%eax"))
                    self.AsmTree.append(Movl("%4(%esp)", "%%ecx"))
                    self.AsmTree.append(Movl("%8(%esp)", "%%edx"))
                    self.AsmTree.append(Addl("&12", "%%esp"))

            elif isinstance(ast, core.Print):
                self.AsmTree.append(Subl("&12", "%%esp"))
                self.AsmTree.append(Movl("%%eax", "%(%esp)"))
                self.AsmTree.append(Movl("%%ecx", "%4(%esp)"))
                self.AsmTree.append(Movl("%%edx", "%8(%esp)"))
                self.AsmTree.append(Push(self.to_base_asm(ast.rhs)))
                # self.AsmTree.append(Movl(self.to_base_asm(ast.rhs), '%(%esp)'))
                self.AsmTree.append(Call("print_int_nl")) 
                self.AsmTree.append(Movl("%4(%esp)", "%%eax"))
                self.AsmTree.append(Movl("%8(%esp)", "%%ecx"))
                self.AsmTree.append(Movl("%12(%esp)", "%%edx"))
                self.AsmTree.append(Addl("&16", "%%esp"))

