# Instruction Selection
#
import core
import platform

def output(ast, fname):
    Print = printer(fname);
    Print.output(ast);


class printer:
    def __init__(self, fileName):
        self.out = open( fileName, 'w' )
        self.namenum = 0
        self.nametrans = {}

    def emit(self, line):
        self.out.write( line + '\n' );

    def output(self, ast):
        self.emit( '.data' );
        self.emit( '.text' );
       
        self.emit( '.globl main' );
        self.emit( '.type main, @function' );
        self.emit( 'main:' );
        
        self.preamble()
        #self.emit( '    subl $%s, %%esp' % (size,)  );
        
        self.printTree(ast)
        
        self.emit('    movl $0, %eax');
        self.emit('    leave');
        self.emit('    ret');

    def printTree(self, lst):
        for instr in lst:
            self.emit( instr._to_str())
        
    def preamble(self):
        self.emit('    pushl %ebp');
        self.emit('    movl %esp, %ebp');
        pass
