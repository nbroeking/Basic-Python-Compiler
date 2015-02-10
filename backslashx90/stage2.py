# 
#

from AsmTree import Movl, Addl, Neg, Push#, Pop, Call, Subl
import core
import platform

def stage2(ast, fname):
    st2 = Stage2(fname);
    st2.assemble(ast);


class Stage2:
    def __init__(self):
        self.namenum = 0
        self.nametrans = {}
        self.AsmTree = []

    # python -> stage1 -> stage2 -> file
    def emit(self, line):
        self.out.write( line + '\n' );

    def assemble(self, ast):
        self.instructionSelection(ast);
        for i in self.AsmTree:
            print ("%s", i._to_str())

    def to_base_asm( self, ast ):
        if isinstance(ast, core.Const):
            return "$%s" % (ast.raw,) 
        elif isinstance(ast, core.Name):
            if( isinstance(ast.name, int) ):
                return self.to_offset(ast.name)
            return ast.name

    def instructionSelection(self, lst):
        for ast in lst:
            if isinstance(ast, core.Assign):
                name = ast.name
                op = ast.rhs
                if isinstance(op, core.Add):
                    self.AsmTree.append(Addl(self.to_base_asm(op.rhs), self.to_base_asm(op.lhs)))

                if isinstance(op, core.Neg):
                    self.AsmTree.append(Neg(self.to_base_asm(op.rhs)))

                elif isinstance(op, core.Const):
                    self.AsmTree.append(Movl(self.to_base_asm(op), name ))
                
                elif isinstance(op, core.Name):
                    self.AsmTree.append(Movl(self.to_base_asm(op), name))

                elif isinstance(op, core.CallFunc):
                    for i in op.args:
                        self.AsmTree.append(Push(self.to_base_asm(i)))

                    self.AsmTree.append(Push(self.to_base_asm(op.lhs)))
                    self.AsmTree.append(Movl("%eax", self.to_offset(name)))

