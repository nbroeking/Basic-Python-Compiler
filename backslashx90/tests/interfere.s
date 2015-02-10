.data
.text
.globl main
.type main, @function
main:
    pushl %ebp
    movl %esp, %ebp
movl $5, %ebx
movl $3, %edx
movl $4, %ecx
movl %ebx, %eax
addl %edx, %eax
movl %eax, %esi
movl %edx, %eax
addl %ebx, %eax
movl %eax, %edi
movl $2, %eax
addl %ebx, %eax
movl %eax, -8(%ebp)
movl $5, %eax
addl -8(%ebp), %eax
movl %eax, -4(%ebp)
movl %ebx, -16(%ebp)
movl %edx, %eax
addl %ebx, %eax
addl -16(%ebp), %eax
movl %eax, -12(%ebp)
movl %ebx, %eax
addl %edx, %eax
addl %ecx, %eax
addl %esi, %eax
addl %edi, %eax
addl -8(%ebp), %eax
addl -4(%ebp), %eax
addl -16(%ebp), %eax
addl -12(%ebp), %eax
    movl $0, %eax
    leave
    ret
