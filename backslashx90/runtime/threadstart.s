    .file "start_thread.s"
    .text
.Ltext0:
    .globl __thread_start
    .type  __thread_start, @function

/* A routine to be able to start our thread
 * Must be an assembly function since there
 * is no way to push a variable number of
 * args on the stack in c */
__thread_start:
    pushl %ebp
    movl %esp, %ebp

    pushl %ebx
    pushl %esi
    pushl %edi

    /* eax, ecx, edx */
    movl 8(%ebp), %eax /* the address of thread_args */
    movl 12(%eax), %edx /* nargs is in edx */
    movl 8(%eax), %esi /* args */
    xorl %ecx, %ecx /* counter */

    /* Allocate space for nargs on the stack as
     * well as the closure. 4 + (0+nargs*4) */
    leal 4(%ecx,%edx,4), %edi
    subl %edi, %esp

.loop:
    cmpl %ecx, %edx /* while ecx < edx */
    jz .end_loop

        movl (%esi, %ecx, 4), %ebx /* move (%esi,%ecx,4) to (%esp,%ecx,-4) */
        movl %ebx, (%esp, %ecx, 4)
        addl $1, %ecx

    jmp .loop
.end_loop:
    /* done pushing arguments onto the stack */
    /* Now put the closure on the stack */
    movl (%eax), %ebx /* ebx = args->fn :: big_pyobj */
    movl 8(%ebx), %ecx /* ecx = closure */
    movl 4(%ebx), %ebx /* load the c-style function */
    movl %ecx, (%esp,%edx,4) /* esp[nargs] = ecx */
    /* stack in order, now call the damn function */

    /* we can finaly call the function, but
     * we need to make sure to put the return
     * value where it is supposed to be */
    movl 4(%eax), %edi /* edi is the return pointer */
    movl %edx, %esi /* move edx into a callee saved register */
    call *%ebx
    movl %eax, (%edi)


    leal 4(%esp,%esi,4), %esp /* restore the stack */

    /* call pthread_exit */
    movl $0, (%esp)
    call pthread_exit

    popl %edi
    popl %esi
    popl %ebx

    leave
    ret
