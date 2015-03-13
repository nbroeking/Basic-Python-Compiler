# Instruction Selection
#
def output(ast, fname, n):
    Print = printer(fname);
    Print.output(ast,n);

def printTree(ast, fname):
    pp = printer(fname);
    pp.printTree(ast)

from function_comb import mangle
try:
    from viper.AsmTree import Label, Raw
except:
    from AsmTree import Label, Raw


class printer:
    def __init__(self, fileName):
        self.out = open( fileName, 'w' )
        self.namenum = 0
        self.nametrans = {}

    def emit(self, line):
        self.out.write( line + '\n' );

    def output(self, ast, nfreevars):
        self.emit( '.data' );
        self.emit( 'puke_msg:' )
        self.emit( '.asciz \"There was a runtime error. PUKE.\\n\"' )
        self.emit( '.text' );
        
        self.emit( 'puke:' )
        self.emit( '    push $puke_msg' )
        self.emit( '    call puts' )
        self.emit( '    movl $127, %eax' )
        self.emit( '    leave' )
        self.emit( '    ret' )
        self.emit( '' )

        self.emit( '.globl main' );
        self.emit( '.type main, @function' );
        self.emit( 'main:' );
        self.emit( '    pushl %ebp' )
        self.emit( '    movl %esp, %ebp' )
        self.emit( '    pushl $' + str(nfreevars*4) )
        self.emit( '    call create_list' )
        self.emit( '    orl  $3, %eax' )
        self.emit( '    movl %eax, (%esp)' )
        self.emit( '    call ' + mangle("", "main") );
        self.emit( '    movl $0, %eax' )
        self.emit( '    leave' )
        self.emit( '    ret' )
        self.emit( '' )
        
        # self.preamble()
        #self.emit( '    subl $%s, %%esp' % (size,)  );
        
        self.printTree(ast)

    def printTree(self, lst):
        for instr in lst:
            if isinstance(instr, (Label,Raw)):
                self.emit(instr._to_str())
            else:
                self.emit('    ' + instr._to_str())
    def preamble(self):
        self.emit('    pushl %ebp');
        self.emit('    movl %esp, %ebp');
        pass
