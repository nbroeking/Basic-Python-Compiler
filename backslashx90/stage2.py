# 
#

import core
import platform

def stage2(ast, fname):
    st2 = Stage2(fname);
    st2.assemble(ast);


class Stage2:
    def __init__(self, fileName):
        self.out = open( fileName, 'w' )
        self.namenum = 0
        self.nametrans = {}

    # python -> stage1 -> stage2 -> file
    def emit(self, line):
        self.out.write( line + '\n' );

    def assemble(self, ast):
        self.emit( '.data' );
        self.emit( '.text' );
       
        if platform.system() == 'Darwin':
            self.emit( '.globl _main')
            self.emit('_main:')
        else:
            self.emit( '.globl main' );
            self.emit( '.type main, @function' );
            self.emit( 'main:' );
        
        size = self.changeNames(ast);
        self.preamble()
        self.emit( '    subl $%s, %%esp' % (size,)  );
        
        # print '---'
        # for i in ast:
        #     print (i._to_str())

        self.instructionSelection(ast);

        self.emit('    movl $0, %eax');
        self.emit('    leave');
        self.emit('    ret');

    def to_offset( self, var ):
        return "-%s(%%ebp)" % (var,)

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
                    self.emit( '    movl %s, %%eax' % self.to_base_asm(op.rhs) );
                    self.emit( '    addl %s, %%eax' % self.to_base_asm(op.lhs) );
                    self.emit( '    movl %%eax, %s' % self.to_offset(name) )
                if isinstance(op, core.Neg):
                    self.emit( '    movl %s, %%eax' % self.to_base_asm(op.rhs) );
                    self.emit( '    negl %eax' );
                    self.emit( '    movl %%eax, %s' % self.to_offset(name) )
                elif isinstance(op, core.Const):
                    self.emit( '    movl %s, %%eax' % self.to_base_asm(op) )
                    self.emit( '    movl %%eax, %s' % self.to_offset(name) )
                elif isinstance(op, core.Name):
                    self.emit( '    movl %s, %%eax' % self.to_base_asm(op) )
                    self.emit( '    movl %%eax, %s' % self.to_offset(name) )
                elif isinstance(op, core.CallFunc):
                    for i in op.args:
                        self.emit( '    push %s' % self.to_base_asm(i) )
                    if platform.system() == 'Darwin':
                        self.emit('    call _%s' % self.to_base_asm(op.lhs))
                    else:
                        self.emit('    call %s' % self.to_base_asm(op.lhs))
                    self.emit('    movl %%eax, %s' % self.to_offset(name))

            elif isinstance(ast, core.Print):
                self.emit( '    movl %s, %%eax' % self.to_base_asm(ast.rhs) )
                self.emit( '    pushl %eax' )
                if platform.system() == 'Darwin':
                    self.emit('    call _print_int_nl')
                else:
                    self.emit('    call print_int_nl' )

    def changeNames(self, ast):
        self.namenum = 4

        def changeName_(stmt):
            if isinstance(stmt, core.Name) or isinstance(stmt, core.Assign):
                if stmt.name in self.nametrans:
                    stmt.name = self.nametrans[stmt.name]
                else:
                    self.nametrans[stmt.name] = self.namenum
                    stmt.name = self.namenum
                    self.namenum += 4

            for i in stmt.children:
                changeName_(i)
                
            
        for i in ast:
            changeName_(i)

        return self.namenum;
        
    def preamble(self):
        self.emit('    pushl %ebp');
        self.emit('    movl %esp, %ebp');
        pass
