.data
.text
.globl main
.type main, @function
main:
    pushl %ebp
    movl %esp, %ebp
movl &1 -> $0$
$0$ += &2
movl $0$ -> x
movl &1 -> $1$
$1$ += &2
movl &3 -> $2$
- None 
movl $2$ -> $3$
- None 
movl $1$ -> $4$
$4$ += $3$
movl &2 -> $5$
- None 
movl $4$ -> $6$
$6$ += $5$
movl &2 -> $7$
- None 
movl &1 -> $8$
$8$ += $7$
movl $6$ -> $9$
$9$ += $8$
movl &1 -> $10$
- None 
movl $9$ -> $11$
$11$ += $10$
movl $11$ -> y
movl y -> $12$
$12$ += x
movl $12$ -> __2yolo12_3_
    movl $0, %eax
    leave
    ret
