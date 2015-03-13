.data
puke_msg:
.asciz "There was a runtime error. PUKE.\n"
.text
puke:
    push $puke_msg
    call puts
    movl $127, %eax
    leave
    ret
.globl main
.type main, @function
main:
   jmp py_main
main_davis:
.long $fn_main_davis
.long 0
fn_main_davis:
    pushl %ebp
    movl %esp, %ebp
    subl $8, %esp
    // True = 0 = %eax
    // False = 0 = %eax
    // End Instruction 


    // *True = 5
    movl $5, %eax
    // End Instruction 


    // *False = 1
    movl $1, %eax
    subl $12, %esp
    movl %eax, (%esp)
    movl %ecx, 4(%esp)
    movl %edx, 8(%esp)
    pushl $16
    call print_any
    movl 4(%esp), %eax
    movl 8(%esp), %ecx
    movl 12(%esp), %edx
    addl $16, %esp
.main_davis_ret:
    leave
    ret
.main:
.long $fn_.main
.long 0
fn_.main:
    pushl %ebp
    movl %esp, %ebp
    subl $8, %esp
    // davis = 0 = %eax
    // True = 0 = %eax
    // $0$ = 1 = %ebx
    // False = 0 = %eax
    // End Instruction 


    // *True = 5
    movl $5, %eax
    // End Instruction 


    // *False = 1
    movl $1, %eax
    // End Instruction 


    // *$0$ = closure(main_davis)
    // End Instruction 


    // *davis = $$0$
    movl %ebx, %eax
    // End Instruction 


    // *$1$ = *$davis()
..main_ret:
    leave
    ret
