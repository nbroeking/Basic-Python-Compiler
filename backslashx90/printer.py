# Instruction Selection
#
def output(ast, fname, n, data_section):
    Print = printer(fname);
    Print.output(ast,n,data_section);

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

    def output(self, ast, nfreevars, data_section):
        self.emit( '.data' );
        self.emit( 'puke_msg:' )
        self.emit( '.asciz \"There was a runtime error. PUKE.\\n\"' )

        self.emit('__init__str__:')
        self.emit('.asciz \"__init__\"')

        for (k, v) in data_section.items():
            self.emit('%s:' % v)
            self.emit('.asciz \"%s\"' % k)

        self.emit( '.text' );

        self.emit( '''
set_subscript2:
    /* cuz i got tired of lookin at it! */
    movl 8(%esp), %eax
    movl %eax, %ecx
    andl $0x3, %ecx
    andl $0xfffffffc, %eax
    cmpl $3, %ecx
    jnz set_subscript /* if not a bigobj */
    movl (%eax), %ecx /* ecx now has the tag */
    cmpl $2, %ecx     /* compare to FUN */
    jnz set_subscript
    movl %eax, 8(%esp)
    jmp set_subscript /* treat functions as ptrs */

    ret               /* just for show */

get_subscript2:
    /* cuz i got tired of lookin at it! */
    movl 8(%esp), %eax
    movl %eax, %ecx
    andl $0x3, %ecx
    andl $0xfffffffc, %eax
    cmpl $3, %ecx
    jnz get_subscript /* if not a bigobj */
    movl (%eax), %ecx /* ecx now has the tag */
    cmpl $2, %ecx     /* compare to FUN */
    jnz get_subscript
    movl %eax, 8(%esp)
    jmp get_subscript /* treat functions as ptrs */

    ret               /* just for show */
        ''')
        
        self.emit( 'puke:' )
        self.emit( '    push $puke_msg' )
        self.emit( '    call puts' )
        self.emit( '    movl $127, (%esp)' )
        self.emit( '    call exit' )
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
