.data
puke_msg:
.asciz "There was a runtime error. PUKE.\n"
0_str:
.asciz "x"
1_str:
.asciz "__init__"
.text

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
        
puke:
    push $puke_msg
    call puts
    movl $127, (%esp)
    call exit
    leave
    ret

.globl main
.type main, @function
main:
    pushl %ebp
    movl %esp, %ebp
    pushl $0
    call create_list
    orl  $3, %eax
    movl %eax, (%esp)
    call x90__main
    movl $0, %eax
    leave
    ret


    /* __init__[x,__init__](self) {  */
.globl x90_x90_x90__main_Basic___init__
.type x90_x90_x90__main_Basic___init__,@function
x90_x90_x90__main_Basic___init__:
    pushl %ebp
    movl %esp, %ebp
    subl $12, %esp
    movl %ebx, -4(%ebp)
    movl %esi, -8(%ebp)
    movl %edi, -12(%ebp)
    subl $8, %esp
    /* $s2_0 = 0 = %eax */
    /* False = 0 = %eax */
    /* $fn_closure = 1 = %ebx */
    /* self = 0 = %eax */
    /* y = 0 = %eax */
    /* x = 2 = %ecx */
    /* True = 0 = %eax */
    /* __init__ = 3 = %edx */
    /* Bringing parent closure into local scope {{{ */
    movl 12(%ebp), %eax
    movl 0x0(%eax), %ecx
    movl 0x4(%eax), %edx
    /* }}} */
    /* Bringing arguments into local scope {{{ */
    movl 8(%ebp), %eax
    /* }}} */
    /* Building local closure {{{ */
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $16, (%esp)
    call malloc
    movl %eax, %ebx
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    /* Updating closure (x) {{{ */
    movl %ecx, 0x4(%ebx)
    /* }}} */
    /* Updating closure (__init__) {{{ */
    movl %edx, 0xc(%ebx)
    /* }}} */
    /* Updating closure (self) {{{ */
    movl %eax, 0x8(%ebx)
    /* }}} */
    /* }}} */
    /* End Instruction 

 */
    /* *True = 5 */
    movl $5, %eax
    /* End Instruction 

 */
    /* *False = 1 */
    movl $1, %eax
    /* End Instruction 

 */
    /* *y = 8 */
    movl $8, %eax
    /* Updating closure (y) {{{ */
    movl %eax, 0x0(%ebx)
    /* }}} */
.x90_x90_x90__main_Basic___init___ret:
    movl -4(%ebp), %ebx
    movl -8(%ebp), %esi
    movl -12(%ebp), %edi
    addl $12, %esp
    leave
    ret
    /* } */

    /* main[]() {  */
.globl x90__main
.type x90__main,@function
x90__main:
    pushl %ebp
    movl %esp, %ebp
    subl $12, %esp
    movl %ebx, -4(%ebp)
    movl %esi, -8(%ebp)
    movl %edi, -12(%ebp)
    subl $8, %esp
    /* $s2_1 = 1 = %ebx */
    /* $s2_0 = 0 = %eax */
    /* False = 0 = %eax */
    /* $fn_closure = 4 = %edi */
    /* $0$ = 1 = %ebx */
    /* Basic = 5 = %esi */
    /* True = 0 = %eax */
    /* Bringing parent closure into local scope {{{ */
    movl 8(%ebp), %eax
    /* }}} */
    /* Bringing arguments into local scope {{{ */
    /* }}} */
    /* Building local closure {{{ */
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $8, (%esp)
    call malloc
    movl %eax, %edi
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    /* }}} */
    /* End Instruction 

 */
    /* *True = 5 */
    movl $5, %eax
    /* End Instruction 

 */
    /* *False = 1 */
    movl $1, %eax
    /* End Instruction 

 */
    /* *Basic = AllocClass() */
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $0, (%esp)
    call create_list
    addl $3, %eax
    movl %eax, %ebx
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl %ebx, (%esp)
    call create_class
    addl $3, %eax
    movl %eax, %esi
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    subl $24, %esp
    movl %eax, 0xc(%esp)
    movl %ecx, 0x10(%esp)
    movl %edx, 0x14(%esp)
    movl %esi, (%esp)
    movl $0_str, 4(%esp)
    movl $4, 8(%esp)
    movl 0xc(%esp), %eax
    movl 0x10(%esp), %ecx
    movl 0x14(%esp), %edx
    addl $24, %esp
    /* End Instruction 

 */
    /* *$0$ = closure(x90_x90_x90__main_Basic___init__) */
    subl $28, %esp
    movl %eax, 0x10(%esp)
    movl %ecx, 0x14(%esp)
    movl %edx, 0x18(%esp)
    movl $x90_x90_x90__main_Basic___init__, (%esp)
    movl %edi, 4(%esp)
    call create_closure
    orl $3, %eax
    movl %eax, %ebx
    movl 0x10(%esp), %eax
    movl 0x14(%esp), %ecx
    movl 0x18(%esp), %edx
    addl $28, %esp
    subl $24, %esp
    movl %eax, 0xc(%esp)
    movl %ecx, 0x10(%esp)
    movl %edx, 0x14(%esp)
    movl %esi, (%esp)
    movl $1_str, 4(%esp)
    movl %ebx, 8(%esp)
    movl 0xc(%esp), %eax
    movl 0x10(%esp), %ecx
    movl 0x14(%esp), %edx
    addl $24, %esp
.x90__main_ret:
    movl -4(%ebp), %ebx
    movl -8(%ebp), %esi
    movl -12(%ebp), %edi
    addl $12, %esp
    leave
    ret
    /* } */
