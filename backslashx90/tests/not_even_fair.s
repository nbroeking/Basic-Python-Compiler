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
    pushl %ebp
    movl %esp, %ebp
    subl $240, %esp
    // $93$ = 1 = %ebx
    // $66$ = 1 = %ebx
    // $83$ = 1 = %ebx
    // $32$ = 32 = -108(%ebp)
    // $50$ = 4 = %edi
    // $77$ = 1 = %ebx
    // $20$ = 27 = -88(%ebp)
    // $46$ = 5 = %esi
    // 41 = 1 = %ebx
    // 24 = 0 = %eax
    // 25 = 0 = %eax
    // 26 = 0 = %eax
    // 27 = 0 = %eax
    // 20 = 0 = %eax
    // 21 = 1 = %ebx
    // 22 = 0 = %eax
    // 23 = 0 = %eax
    // 28 = 0 = %eax
    // 29 = 0 = %eax
    // $4$ = 6 = -4(%ebp)
    // 0 = 0 = %eax
    // 4 = 0 = %eax
    // 8 = 1 = %ebx
    // $data_ptr_43 = 2 = %ecx
    // $16$ = 29 = -96(%ebp)
    // $data_ptr_47 = 36 = -124(%ebp)
    // $92$ = 1 = %ebx
    // $67$ = 1 = %ebx
    // 120 = 0 = %eax
    // $76$ = 1 = %ebx
    // False = 0 = %eax
    // 59 = 0 = %eax
    // 58 = 1 = %ebx
    // 55 = 0 = %eax
    // 54 = 1 = %ebx
    // 57 = 0 = %eax
    // 56 = 1 = %ebx
    // 51 = 0 = %eax
    // 50 = 1 = %ebx
    // 53 = 0 = %eax
    // 52 = 1 = %ebx
    // $84$ = 1 = %ebx
    // $62$ = 20 = -60(%ebp)
    // $26$ = 16 = -44(%ebp)
    // $71$ = 1 = %ebx
    // $89$ = 1 = %ebx
    // $40$ = 7 = -8(%ebp)
    // $88$ = 1 = %ebx
    // $91$ = 1 = %ebx
    // $64$ = 1 = %ebx
    // 115 = 1 = %ebx
    // 114 = 0 = %eax
    // 88 = 0 = %eax
    // 89 = 0 = %eax
    // 111 = 1 = %ebx
    // 110 = 0 = %eax
    // 113 = 0 = %eax
    // 112 = 0 = %eax
    // 82 = 0 = %eax
    // 83 = 0 = %eax
    // 80 = 0 = %eax
    // 81 = 0 = %eax
    // 119 = 0 = %eax
    // 118 = 0 = %eax
    // 84 = 0 = %eax
    // 85 = 0 = %eax
    // $data_ptr_5 = 39 = -136(%ebp)
    // $36$ = 9 = -16(%ebp)
    // $data_ptr_7 = 40 = -140(%ebp)
    // $data_ptr_1 = 41 = -144(%ebp)
    // $data_ptr_3 = 42 = -148(%ebp)
    // $6$ = 10 = -20(%ebp)
    // $24$ = 11 = -24(%ebp)
    // $data_ptr_9 = 43 = -152(%ebp)
    // $48$ = 12 = -28(%ebp)
    // 3 = 0 = %eax
    // 7 = 0 = %eax
    // $85$ = 1 = %ebx
    // True = 0 = %eax
    // $70$ = 1 = %ebx
    // $14$ = 13 = -32(%ebp)
    // $90$ = 1 = %ebx
    // $38$ = 14 = -36(%ebp)
    // $65$ = 1 = %ebx
    // 108 = 0 = %eax
    // 109 = 0 = %eax
    // x = 0 = %eax
    // 102 = 0 = %eax
    // 103 = 0 = %eax
    // 100 = 0 = %eax
    // 101 = 0 = %eax
    // 106 = 0 = %eax
    // 107 = 1 = %ebx
    // 104 = 0 = %eax
    // 105 = 0 = %eax
    // 39 = 1 = %ebx
    // 38 = 1 = %ebx
    // 33 = 0 = %eax
    // 32 = 0 = %eax
    // 31 = 1 = %ebx
    // 30 = 0 = %eax
    // 37 = 1 = %ebx
    // 36 = 0 = %eax
    // 35 = 0 = %eax
    // 34 = 0 = %eax
    // $data_ptr_59 = 44 = -156(%ebp)
    // $data_ptr_55 = 45 = -160(%ebp)
    // $data_ptr_57 = 46 = -164(%ebp)
    // $data_ptr_51 = 47 = -168(%ebp)
    // $86$ = 1 = %ebx
    // $10$ = 34 = -116(%ebp)
    // $87$ = 1 = %ebx
    // $73$ = 1 = %ebx
    // $data_ptr_45 = 37 = -128(%ebp)
    // $42$ = 18 = -52(%ebp)
    // $18$ = 19 = -56(%ebp)
    // 60 = 0 = %eax
    // 61 = 0 = %eax
    // 62 = 1 = %ebx
    // 63 = 0 = %eax
    // 64 = 0 = %eax
    // 65 = 0 = %eax
    // 66 = 1 = %ebx
    // 67 = 0 = %eax
    // 68 = 1 = %ebx
    // 69 = 0 = %eax
    // $54$ = 21 = -64(%ebp)
    // $8$ = 17 = -48(%ebp)
    // $30$ = 22 = -68(%ebp)
    // $data_ptr_29 = 49 = -176(%ebp)
    // 2 = 1 = %ebx
    // 6 = 1 = %ebx
    // $data_ptr_21 = 50 = -180(%ebp)
    // $data_ptr_23 = 51 = -184(%ebp)
    // $data_ptr_25 = 52 = -188(%ebp)
    // $data_ptr_27 = 53 = -192(%ebp)
    // $52$ = 28 = -92(%ebp)
    // $80$ = 1 = %ebx
    // $28$ = 23 = -72(%ebp)
    // $0$ = 24 = -76(%ebp)
    // $12$ = 25 = -80(%ebp)
    // 99 = 0 = %eax
    // 98 = 0 = %eax
    // $58$ = 26 = -84(%ebp)
    // 91 = 0 = %eax
    // 90 = 0 = %eax
    // 93 = 0 = %eax
    // 92 = 0 = %eax
    // 95 = 0 = %eax
    // 94 = 1 = %ebx
    // 97 = 0 = %eax
    // 96 = 0 = %eax
    // 11 = 1 = %ebx
    // 10 = 1 = %ebx
    // 13 = 1 = %ebx
    // 12 = 2 = %ecx
    // 15 = 1 = %ebx
    // 14 = 1 = %ebx
    // 17 = 0 = %eax
    // 16 = 2 = %ecx
    // 19 = 1 = %ebx
    // 18 = 1 = %ebx
    // $22$ = 15 = -40(%ebp)
    // 117 = 1 = %ebx
    // $data_ptr_39 = 54 = -196(%ebp)
    // 116 = 0 = %eax
    // $data_ptr_33 = 55 = -200(%ebp)
    // $data_ptr_31 = 56 = -204(%ebp)
    // $96$ = 1 = %ebx
    // $data_ptr_37 = 57 = -208(%ebp)
    // $data_ptr_35 = 58 = -212(%ebp)
    // $68$ = 1 = %ebx
    // $81$ = 1 = %ebx
    // $56$ = 8 = -12(%ebp)
    // $75$ = 1 = %ebx
    // $79$ = 1 = %ebx
    // $data_ptr_41 = 3 = %edx
    // $44$ = 30 = -100(%ebp)
    // $60$ = 31 = -104(%ebp)
    // 48 = 1 = %ebx
    // 49 = 1 = %ebx
    // 46 = 1 = %ebx
    // 86 = 0 = %eax
    // 44 = 0 = %eax
    // 45 = 1 = %ebx
    // 42 = 1 = %ebx
    // 43 = 0 = %eax
    // 40 = 1 = %ebx
    // 87 = 0 = %eax
    // 1 = 0 = %eax
    // 5 = 0 = %eax
    // $78$ = 1 = %ebx
    // $72$ = 1 = %ebx
    // 9 = 0 = %eax
    // $2$ = 33 = -112(%ebp)
    // $95$ = 1 = %ebx
    // $94$ = 1 = %ebx
    // $data_ptr_49 = 38 = -132(%ebp)
    // $69$ = 1 = %ebx
    // $data_ptr_63 = 1 = %ebx
    // $82$ = 1 = %ebx
    // $74$ = 1 = %ebx
    // 77 = 0 = %eax
    // 76 = 0 = %eax
    // 75 = 1 = %ebx
    // 74 = 0 = %eax
    // 73 = 0 = %eax
    // 72 = 1 = %ebx
    // 71 = 0 = %eax
    // 70 = 1 = %ebx
    // $34$ = 35 = -120(%ebp)
    // 79 = 0 = %eax
    // 78 = 0 = %eax
    // $data_ptr_61 = 59 = -216(%ebp)
    // $data_ptr_11 = 60 = -220(%ebp)
    // $data_ptr_13 = 61 = -224(%ebp)
    // $data_ptr_15 = 62 = -228(%ebp)
    // $data_ptr_53 = 48 = -172(%ebp)
    // $data_ptr_17 = 63 = -232(%ebp)
    // 47 = 1 = %ebx
    // $data_ptr_19 = 64 = -236(%ebp)
    // End Instruction 


    // *True = 5
    movl $5, %eax
    // End Instruction 


    // *False = 1
    movl $1, %eax
    // End Instruction 


    // *$0$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -76(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_1 = 0x4($0$)
    // Spilling source Deref movl 0x4($0$), $data_ptr_1
    movl -76(%ebp), %eax
    // Spilling memory movl 0x4(0), $data_ptr_1
    movl 0x4(%eax), %eax
    movl %eax, -144(%ebp)
    // End spill memory movl 0x4(0), $data_ptr_1
    //  end Deref
    // End Instruction 


    // *0x8($0$) = 1
    // Spilling destination Deref movl $1, 0x8($0$)
    movl -76(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$2$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -112(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_3 = 0x4($2$)
    // Spilling source Deref movl 0x4($2$), $data_ptr_3
    movl -112(%ebp), %ebx
    // Spilling memory movl 0x4(2), $data_ptr_3
    movl 0x4(%ebx), %eax
    movl %eax, -148(%ebp)
    // End spill memory movl 0x4(2), $data_ptr_3
    //  end Deref
    // End Instruction 


    // *0x8($2$) = 1
    // Spilling destination Deref movl $1, 0x8($2$)
    movl -112(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$4$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -4(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_5 = 0x4($4$)
    // Spilling source Deref movl 0x4($4$), $data_ptr_5
    movl -4(%ebp), %eax
    // Spilling memory movl 0x4(4), $data_ptr_5
    movl 0x4(%eax), %ebx
    movl %ebx, -136(%ebp)
    // End spill memory movl 0x4(4), $data_ptr_5
    //  end Deref
    // End Instruction 


    // *0x8($4$) = 1
    // Spilling destination Deref movl $1, 0x8($4$)
    movl -4(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$6$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -20(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_7 = 0x4($6$)
    // Spilling source Deref movl 0x4($6$), $data_ptr_7
    movl -20(%ebp), %ebx
    // Spilling memory movl 0x4(6), $data_ptr_7
    movl 0x4(%ebx), %eax
    movl %eax, -140(%ebp)
    // End spill memory movl 0x4(6), $data_ptr_7
    //  end Deref
    // End Instruction 


    // *0x8($6$) = 1
    // Spilling destination Deref movl $1, 0x8($6$)
    movl -20(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$8$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -48(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_9 = 0x4($8$)
    // Spilling source Deref movl 0x4($8$), $data_ptr_9
    movl -48(%ebp), %ebx
    // Spilling memory movl 0x4(8), $data_ptr_9
    movl 0x4(%ebx), %eax
    movl %eax, -152(%ebp)
    // End spill memory movl 0x4(8), $data_ptr_9
    //  end Deref
    // End Instruction 


    // *0x8($8$) = 1
    // Spilling destination Deref movl $1, 0x8($8$)
    movl -48(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$10$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -116(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_11 = 0x4($10$)
    // Spilling source Deref movl 0x4($10$), $data_ptr_11
    movl -116(%ebp), %ebx
    // Spilling memory movl 0x4(10), $data_ptr_11
    movl 0x4(%ebx), %eax
    movl %eax, -220(%ebp)
    // End spill memory movl 0x4(10), $data_ptr_11
    //  end Deref
    // End Instruction 


    // *0x8($10$) = 1
    // Spilling destination Deref movl $1, 0x8($10$)
    movl -116(%ebp), %ebx
    movl $1, 0x8(%ebx)
    //  end Deref
    // End Instruction 


    // *$12$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -80(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_13 = 0x4($12$)
    // Spilling source Deref movl 0x4($12$), $data_ptr_13
    movl -80(%ebp), %ecx
    // Spilling memory movl 0x4(12), $data_ptr_13
    movl 0x4(%ecx), %ebx
    movl %ebx, -224(%ebp)
    // End spill memory movl 0x4(12), $data_ptr_13
    //  end Deref
    // End Instruction 


    // *0x8($12$) = 1
    // Spilling destination Deref movl $1, 0x8($12$)
    movl -80(%ebp), %ebx
    movl $1, 0x8(%ebx)
    //  end Deref
    // End Instruction 


    // *$14$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -32(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_15 = 0x4($14$)
    // Spilling source Deref movl 0x4($14$), $data_ptr_15
    movl -32(%ebp), %ebx
    // Spilling memory movl 0x4(14), $data_ptr_15
    movl 0x4(%ebx), %eax
    movl %eax, -228(%ebp)
    // End spill memory movl 0x4(14), $data_ptr_15
    //  end Deref
    // End Instruction 


    // *0x8($14$) = 1
    // Spilling destination Deref movl $1, 0x8($14$)
    movl -32(%ebp), %ebx
    movl $1, 0x8(%ebx)
    //  end Deref
    // End Instruction 


    // *$16$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -96(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_17 = 0x4($16$)
    // Spilling source Deref movl 0x4($16$), $data_ptr_17
    movl -96(%ebp), %ecx
    // Spilling memory movl 0x4(16), $data_ptr_17
    movl 0x4(%ecx), %ebx
    movl %ebx, -232(%ebp)
    // End spill memory movl 0x4(16), $data_ptr_17
    //  end Deref
    // End Instruction 


    // *0x8($16$) = 1
    // Spilling destination Deref movl $1, 0x8($16$)
    movl -96(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$18$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -56(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_19 = 0x4($18$)
    // Spilling source Deref movl 0x4($18$), $data_ptr_19
    movl -56(%ebp), %ebx
    // Spilling memory movl 0x4(18), $data_ptr_19
    movl 0x4(%ebx), %eax
    movl %eax, -236(%ebp)
    // End spill memory movl 0x4(18), $data_ptr_19
    //  end Deref
    // End Instruction 


    // *0x8($18$) = 1
    // Spilling destination Deref movl $1, 0x8($18$)
    movl -56(%ebp), %ebx
    movl $1, 0x8(%ebx)
    //  end Deref
    // End Instruction 


    // *$20$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -88(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_21 = 0x4($20$)
    // Spilling source Deref movl 0x4($20$), $data_ptr_21
    movl -88(%ebp), %eax
    // Spilling memory movl 0x4(20), $data_ptr_21
    movl 0x4(%eax), %ebx
    movl %ebx, -180(%ebp)
    // End spill memory movl 0x4(20), $data_ptr_21
    //  end Deref
    // End Instruction 


    // *0x8($20$) = 1
    // Spilling destination Deref movl $1, 0x8($20$)
    movl -88(%ebp), %ebx
    movl $1, 0x8(%ebx)
    //  end Deref
    // End Instruction 


    // *$22$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -40(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_23 = 0x4($22$)
    // Spilling source Deref movl 0x4($22$), $data_ptr_23
    movl -40(%ebp), %eax
    // Spilling memory movl 0x4(22), $data_ptr_23
    movl 0x4(%eax), %ebx
    movl %ebx, -184(%ebp)
    // End spill memory movl 0x4(22), $data_ptr_23
    //  end Deref
    // End Instruction 


    // *0x8($22$) = 1
    // Spilling destination Deref movl $1, 0x8($22$)
    movl -40(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$24$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -24(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_25 = 0x4($24$)
    // Spilling source Deref movl 0x4($24$), $data_ptr_25
    movl -24(%ebp), %eax
    // Spilling memory movl 0x4(24), $data_ptr_25
    movl 0x4(%eax), %ecx
    movl %ecx, -188(%ebp)
    // End spill memory movl 0x4(24), $data_ptr_25
    //  end Deref
    // End Instruction 


    // *0x8($24$) = 1
    // Spilling destination Deref movl $1, 0x8($24$)
    movl -24(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$26$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -44(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_27 = 0x4($26$)
    // Spilling memory movl 0x4($26$), $data_ptr_27
    // Spilling source Deref movl 0x4($26$), 26
    movl -44(%ebp), %ebx
    movl 0x4(%ebx), %eax
    //  end Deref
    movl %eax, -192(%ebp)
    // End spill memory movl 0x4($26$), $data_ptr_27
    // End Instruction 


    // *0x8($26$) = 1
    // Spilling destination Deref movl $1, 0x8($26$)
    movl -44(%ebp), %ebx
    movl $1, 0x8(%ebx)
    //  end Deref
    // End Instruction 


    // *$28$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -72(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_29 = 0x4($28$)
    // Spilling source Deref movl 0x4($28$), $data_ptr_29
    movl -72(%ebp), %eax
    // Spilling memory movl 0x4(27), $data_ptr_29
    movl 0x4(%eax), %ebx
    movl %ebx, -176(%ebp)
    // End spill memory movl 0x4(27), $data_ptr_29
    //  end Deref
    // End Instruction 


    // *0x8($28$) = 1
    // Spilling destination Deref movl $1, 0x8($28$)
    movl -72(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$30$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -68(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_31 = 0x4($30$)
    // Spilling source Deref movl 0x4($30$), $data_ptr_31
    movl -68(%ebp), %eax
    // Spilling memory movl 0x4(29), $data_ptr_31
    movl 0x4(%eax), %ecx
    movl %ecx, -204(%ebp)
    // End spill memory movl 0x4(29), $data_ptr_31
    //  end Deref
    // End Instruction 


    // *0x8($30$) = 1
    // Spilling destination Deref movl $1, 0x8($30$)
    movl -68(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$32$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -108(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_33 = 0x4($32$)
    // Spilling source Deref movl 0x4($32$), $data_ptr_33
    movl -108(%ebp), %ebx
    // Spilling memory movl 0x4(31), $data_ptr_33
    movl 0x4(%ebx), %eax
    movl %eax, -200(%ebp)
    // End spill memory movl 0x4(31), $data_ptr_33
    //  end Deref
    // End Instruction 


    // *0x8($32$) = 1
    // Spilling destination Deref movl $1, 0x8($32$)
    movl -108(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$34$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -120(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_35 = 0x4($34$)
    // Spilling source Deref movl 0x4($34$), $data_ptr_35
    movl -120(%ebp), %eax
    // Spilling memory movl 0x4(33), $data_ptr_35
    movl 0x4(%eax), %ebx
    movl %ebx, -212(%ebp)
    // End spill memory movl 0x4(33), $data_ptr_35
    //  end Deref
    // End Instruction 


    // *0x8($34$) = 1
    // Spilling destination Deref movl $1, 0x8($34$)
    movl -120(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$36$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -16(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_37 = 0x4($36$)
    // Spilling source Deref movl 0x4($36$), $data_ptr_37
    movl -16(%ebp), %eax
    // Spilling memory movl 0x4(35), $data_ptr_37
    movl 0x4(%eax), %ebx
    movl %ebx, -208(%ebp)
    // End spill memory movl 0x4(35), $data_ptr_37
    //  end Deref
    // End Instruction 


    // *0x8($36$) = 1
    // Spilling destination Deref movl $1, 0x8($36$)
    movl -16(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$38$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -36(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_39 = 0x4($38$)
    // Spilling source Deref movl 0x4($38$), $data_ptr_39
    movl -36(%ebp), %ebx
    // Spilling memory movl 0x4(37), $data_ptr_39
    movl 0x4(%ebx), %eax
    movl %eax, -196(%ebp)
    // End spill memory movl 0x4(37), $data_ptr_39
    //  end Deref
    // End Instruction 


    // *0x8($38$) = 1
    // Spilling destination Deref movl $1, 0x8($38$)
    movl -36(%ebp), %ebx
    movl $1, 0x8(%ebx)
    //  end Deref
    // End Instruction 


    // *$40$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -8(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_41 = 0x4($40$)
    // Spilling source Deref movl 0x4($40$), $data_ptr_41
    movl -8(%ebp), %ebx
    movl 0x4(%ebx), %edx
    //  end Deref
    // End Instruction 


    // *0x8($40$) = 1
    // Spilling destination Deref movl $1, 0x8($40$)
    movl -8(%ebp), %ebx
    movl $1, 0x8(%ebx)
    //  end Deref
    // End Instruction 


    // *$42$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -52(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_43 = 0x4($42$)
    // Spilling source Deref movl 0x4($42$), $data_ptr_43
    movl -52(%ebp), %ebx
    movl 0x4(%ebx), %ecx
    //  end Deref
    // End Instruction 


    // *0x8($42$) = 1
    // Spilling destination Deref movl $1, 0x8($42$)
    movl -52(%ebp), %ebx
    movl $1, 0x8(%ebx)
    //  end Deref
    // End Instruction 


    // *$44$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -100(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_45 = 0x4($44$)
    // Spilling source Deref movl 0x4($44$), $data_ptr_45
    movl -100(%ebp), %eax
    // Spilling memory movl 0x4(43), $data_ptr_45
    movl 0x4(%eax), %ebx
    movl %ebx, -128(%ebp)
    // End spill memory movl 0x4(43), $data_ptr_45
    //  end Deref
    // End Instruction 


    // *0x8($44$) = 1
    // Spilling destination Deref movl $1, 0x8($44$)
    movl -100(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$46$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, %esi
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_47 = 0x4($46$)
    // Spilling memory movl 0x4($46$), $data_ptr_47
    movl 0x4(%esi), %eax
    movl %eax, -124(%ebp)
    // End spill memory movl 0x4($46$), $data_ptr_47
    // End Instruction 


    // *0x8($46$) = 1
    movl $1, 0x8(%esi)
    // End Instruction 


    // *$48$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -28(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_49 = 0x4($48$)
    // Spilling source Deref movl 0x4($48$), $data_ptr_49
    movl -28(%ebp), %ebx
    // Spilling memory movl 0x4(45), $data_ptr_49
    movl 0x4(%ebx), %eax
    movl %eax, -132(%ebp)
    // End spill memory movl 0x4(45), $data_ptr_49
    //  end Deref
    // End Instruction 


    // *0x8($48$) = 1
    // Spilling destination Deref movl $1, 0x8($48$)
    movl -28(%ebp), %ebx
    movl $1, 0x8(%ebx)
    //  end Deref
    // End Instruction 


    // *$50$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, %edi
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_51 = 0x4($50$)
    // Spilling memory movl 0x4($50$), $data_ptr_51
    movl 0x4(%edi), %ebx
    movl %ebx, -168(%ebp)
    // End spill memory movl 0x4($50$), $data_ptr_51
    // End Instruction 


    // *0x8($50$) = 1
    movl $1, 0x8(%edi)
    // End Instruction 


    // *$52$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -92(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_53 = 0x4($52$)
    // Spilling source Deref movl 0x4($52$), $data_ptr_53
    movl -92(%ebp), %ebx
    // Spilling memory movl 0x4(48), $data_ptr_53
    movl 0x4(%ebx), %eax
    movl %eax, -172(%ebp)
    // End spill memory movl 0x4(48), $data_ptr_53
    //  end Deref
    // End Instruction 


    // *0x8($52$) = 1
    // Spilling destination Deref movl $1, 0x8($52$)
    movl -92(%ebp), %ebx
    movl $1, 0x8(%ebx)
    //  end Deref
    // End Instruction 


    // *$54$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -64(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_55 = 0x4($54$)
    // Spilling source Deref movl 0x4($54$), $data_ptr_55
    movl -64(%ebp), %ebx
    // Spilling memory movl 0x4(50), $data_ptr_55
    movl 0x4(%ebx), %eax
    movl %eax, -160(%ebp)
    // End spill memory movl 0x4(50), $data_ptr_55
    //  end Deref
    // End Instruction 


    // *0x8($54$) = 1
    // Spilling destination Deref movl $1, 0x8($54$)
    movl -64(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$56$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -12(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_57 = 0x4($56$)
    // Spilling source Deref movl 0x4($56$), $data_ptr_57
    movl -12(%ebp), %ebx
    // Spilling memory movl 0x4(52), $data_ptr_57
    movl 0x4(%ebx), %eax
    movl %eax, -164(%ebp)
    // End spill memory movl 0x4(52), $data_ptr_57
    //  end Deref
    // End Instruction 


    // *0x8($56$) = 1
    // Spilling destination Deref movl $1, 0x8($56$)
    movl -12(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$58$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -84(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_59 = 0x4($58$)
    // Spilling source Deref movl 0x4($58$), $data_ptr_59
    movl -84(%ebp), %ebx
    // Spilling memory movl 0x4(54), $data_ptr_59
    movl 0x4(%ebx), %eax
    movl %eax, -156(%ebp)
    // End spill memory movl 0x4(54), $data_ptr_59
    //  end Deref
    // End Instruction 


    // *0x8($58$) = 1
    // Spilling destination Deref movl $1, 0x8($58$)
    movl -84(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$60$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -104(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_61 = 0x4($60$)
    // Spilling source Deref movl 0x4($60$), $data_ptr_61
    movl -104(%ebp), %ebx
    // Spilling memory movl 0x4(56), $data_ptr_61
    movl 0x4(%ebx), %eax
    movl %eax, -216(%ebp)
    // End spill memory movl 0x4(56), $data_ptr_61
    //  end Deref
    // End Instruction 


    // *0x8($60$) = 1
    // Spilling destination Deref movl $1, 0x8($60$)
    movl -104(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *$62$ = $create_list(4)
    subl $16, %esp
    movl %eax, 0x4(%esp)
    movl %ecx, 0x8(%esp)
    movl %edx, 0xc(%esp)
    movl $4, 0x0(%esp)
    call create_list
    movl %eax, -60(%ebp)
    movl 0x4(%esp), %eax
    movl 0x8(%esp), %ecx
    movl 0xc(%esp), %edx
    addl $16, %esp
    // End Instruction 


    // *$data_ptr_63 = 0x4($62$)
    // Spilling source Deref movl 0x4($62$), $data_ptr_63
    movl -60(%ebp), %ebx
    // Spilling memory movl 0x4(58), $data_ptr_63
    movl 0x4(%ebx), %eax
    movl %eax, %ebx
    // End spill memory movl 0x4(58), $data_ptr_63
    //  end Deref
    // End Instruction 


    // *0x8($62$) = 1
    // Spilling destination Deref movl $1, 0x8($62$)
    movl -60(%ebp), %eax
    movl $1, 0x8(%eax)
    //  end Deref
    // End Instruction 


    // *0x0($data_ptr_63) = 0
    // Spilling destination Deref movl $0, 0x0($data_ptr_63)
    movl %ebx, %eax
    movl $0, 0x0(%eax)
    //  end Deref
    // End Instruction 


    // *$62$ = ($$62$ + 3)
    // Spilling memory movl $62$, $62$
    // End spill memory movl $62$, $62$
    addl $3, -60(%ebp)
    // End Instruction 


    // *0x0($data_ptr_61) = $$62$
    // Spilling destination Deref movl $62$, 0x0($data_ptr_61)
    movl -216(%ebp), %ebx
    // Spilling memory movl $62$, 0x0(62)
    movl -60(%ebp), %eax
    movl %eax, 0x0(%ebx)
    // End spill memory movl $62$, 0x0(62)
    //  end Deref
    // End Instruction 


    // *$60$ = ($$60$ + 3)
    // Spilling memory movl $60$, $60$
    // End spill memory movl $60$, $60$
    addl $3, -104(%ebp)
    // End Instruction 


    // *0x0($data_ptr_59) = $$60$
    // Spilling destination Deref movl $60$, 0x0($data_ptr_59)
    movl -156(%ebp), %eax
    // Spilling memory movl $60$, 0x0(64)
    movl -104(%ebp), %ebx
    movl %ebx, 0x0(%eax)
    // End spill memory movl $60$, 0x0(64)
    //  end Deref
    // End Instruction 


    // *$58$ = ($$58$ + 3)
    // Spilling memory movl $58$, $58$
    // End spill memory movl $58$, $58$
    addl $3, -84(%ebp)
    // End Instruction 


    // *0x0($data_ptr_57) = $$58$
    // Spilling destination Deref movl $58$, 0x0($data_ptr_57)
    movl -164(%ebp), %ebx
    // Spilling memory movl $58$, 0x0(66)
    movl -84(%ebp), %eax
    movl %eax, 0x0(%ebx)
    // End spill memory movl $58$, 0x0(66)
    //  end Deref
    // End Instruction 


    // *$56$ = ($$56$ + 3)
    // Spilling memory movl $56$, $56$
    // End spill memory movl $56$, $56$
    addl $3, -12(%ebp)
    // End Instruction 


    // *0x0($data_ptr_55) = $$56$
    // Spilling destination Deref movl $56$, 0x0($data_ptr_55)
    movl -160(%ebp), %ebx
    // Spilling memory movl $56$, 0x0(68)
    movl -12(%ebp), %eax
    movl %eax, 0x0(%ebx)
    // End spill memory movl $56$, 0x0(68)
    //  end Deref
    // End Instruction 


    // *$54$ = ($$54$ + 3)
    // Spilling memory movl $54$, $54$
    // End spill memory movl $54$, $54$
    addl $3, -64(%ebp)
    // End Instruction 


    // *0x0($data_ptr_53) = $$54$
    // Spilling destination Deref movl $54$, 0x0($data_ptr_53)
    movl -172(%ebp), %ebx
    // Spilling memory movl $54$, 0x0(70)
    movl -64(%ebp), %eax
    movl %eax, 0x0(%ebx)
    // End spill memory movl $54$, 0x0(70)
    //  end Deref
    // End Instruction 


    // *$52$ = ($$52$ + 3)
    // Spilling memory movl $52$, $52$
    // End spill memory movl $52$, $52$
    addl $3, -92(%ebp)
    // End Instruction 


    // *0x0($data_ptr_51) = $$52$
    // Spilling destination Deref movl $52$, 0x0($data_ptr_51)
    movl -168(%ebp), %ebx
    // Spilling memory movl $52$, 0x0(72)
    movl -92(%ebp), %eax
    movl %eax, 0x0(%ebx)
    // End spill memory movl $52$, 0x0(72)
    //  end Deref
    // End Instruction 


    // *$50$ = ($$50$ + 3)
    movl %edi, %edi
    addl $3, %edi
    // End Instruction 


    // *0x0($data_ptr_49) = $$50$
    // Spilling destination Deref movl $50$, 0x0($data_ptr_49)
    movl -132(%ebp), %eax
    movl %edi, 0x0(%eax)
    //  end Deref
    // End Instruction 


    // *$48$ = ($$48$ + 3)
    // Spilling memory movl $48$, $48$
    // End spill memory movl $48$, $48$
    addl $3, -28(%ebp)
    // End Instruction 


    // *0x0($data_ptr_47) = $$48$
    // Spilling memory movl $48$, 0x0($data_ptr_47)
    movl -28(%ebp), %ebx
    // Spilling destination Deref movl 75, 0x0($data_ptr_47)
    movl -124(%ebp), %eax
    movl %ebx, 0x0(%eax)
    //  end Deref
    // End spill memory movl $48$, 0x0($data_ptr_47)
    // End Instruction 


    // *$46$ = ($$46$ + 3)
    movl %esi, %esi
    addl $3, %esi
    // End Instruction 


    // *0x0($data_ptr_45) = $$46$
    // Spilling destination Deref movl $46$, 0x0($data_ptr_45)
    movl -128(%ebp), %eax
    movl %esi, 0x0(%eax)
    //  end Deref
    // End Instruction 


    // *$44$ = ($$44$ + 3)
    // Spilling memory movl $44$, $44$
    // End spill memory movl $44$, $44$
    addl $3, -100(%ebp)
    // End Instruction 


    // *0x0($data_ptr_43) = $$44$
    // Spilling memory movl $44$, 0x0($data_ptr_43)
    movl -100(%ebp), %eax
    movl %eax, 0x0(%ecx)
    // End spill memory movl $44$, 0x0($data_ptr_43)
    // End Instruction 


    // *$42$ = ($$42$ + 3)
    // Spilling memory movl $42$, $42$
    // End spill memory movl $42$, $42$
    addl $3, -52(%ebp)
    // End Instruction 


    // *0x0($data_ptr_41) = $$42$
    // Spilling memory movl $42$, 0x0($data_ptr_41)
    movl -52(%ebp), %eax
    movl %eax, 0x0(%edx)
    // End spill memory movl $42$, 0x0($data_ptr_41)
    // End Instruction 


    // *$40$ = ($$40$ + 3)
    // Spilling memory movl $40$, $40$
    // End spill memory movl $40$, $40$
    addl $3, -8(%ebp)
    // End Instruction 


    // *0x0($data_ptr_39) = $$40$
    // Spilling destination Deref movl $40$, 0x0($data_ptr_39)
    movl -196(%ebp), %eax
    // Spilling memory movl $40$, 0x0(82)
    movl -8(%ebp), %ebx
    movl %ebx, 0x0(%eax)
    // End spill memory movl $40$, 0x0(82)
    //  end Deref
    // End Instruction 


    // *$38$ = ($$38$ + 3)
    // Spilling memory movl $38$, $38$
    // End spill memory movl $38$, $38$
    addl $3, -36(%ebp)
    // End Instruction 


    // *0x0($data_ptr_37) = $$38$
    // Spilling destination Deref movl $38$, 0x0($data_ptr_37)
    movl -208(%ebp), %eax
    // Spilling memory movl $38$, 0x0(84)
    movl -36(%ebp), %ebx
    movl %ebx, 0x0(%eax)
    // End spill memory movl $38$, 0x0(84)
    //  end Deref
    // End Instruction 


    // *$36$ = ($$36$ + 3)
    // Spilling memory movl $36$, $36$
    // End spill memory movl $36$, $36$
    addl $3, -16(%ebp)
    // End Instruction 


    // *0x0($data_ptr_35) = $$36$
    // Spilling destination Deref movl $36$, 0x0($data_ptr_35)
    movl -212(%ebp), %eax
    // Spilling memory movl $36$, 0x0(86)
    movl -16(%ebp), %ebx
    movl %ebx, 0x0(%eax)
    // End spill memory movl $36$, 0x0(86)
    //  end Deref
    // End Instruction 


    // *$34$ = ($$34$ + 3)
    // Spilling memory movl $34$, $34$
    // End spill memory movl $34$, $34$
    addl $3, -120(%ebp)
    // End Instruction 


    // *0x0($data_ptr_33) = $$34$
    // Spilling destination Deref movl $34$, 0x0($data_ptr_33)
    movl -200(%ebp), %eax
    // Spilling memory movl $34$, 0x0(88)
    movl -120(%ebp), %ebx
    movl %ebx, 0x0(%eax)
    // End spill memory movl $34$, 0x0(88)
    //  end Deref
    // End Instruction 


    // *$32$ = ($$32$ + 3)
    // Spilling memory movl $32$, $32$
    // End spill memory movl $32$, $32$
    addl $3, -108(%ebp)
    // End Instruction 


    // *0x0($data_ptr_31) = $$32$
    // Spilling destination Deref movl $32$, 0x0($data_ptr_31)
    movl -204(%ebp), %eax
    // Spilling memory movl $32$, 0x0(90)
    movl -108(%ebp), %ebx
    movl %ebx, 0x0(%eax)
    // End spill memory movl $32$, 0x0(90)
    //  end Deref
    // End Instruction 


    // *$30$ = ($$30$ + 3)
    // Spilling memory movl $30$, $30$
    // End spill memory movl $30$, $30$
    addl $3, -68(%ebp)
    // End Instruction 


    // *0x0($data_ptr_29) = $$30$
    // Spilling destination Deref movl $30$, 0x0($data_ptr_29)
    movl -176(%ebp), %eax
    // Spilling memory movl $30$, 0x0(92)
    movl -68(%ebp), %ebx
    movl %ebx, 0x0(%eax)
    // End spill memory movl $30$, 0x0(92)
    //  end Deref
    // End Instruction 


    // *$28$ = ($$28$ + 3)
    // Spilling memory movl $28$, $28$
    // End spill memory movl $28$, $28$
    addl $3, -72(%ebp)
    // End Instruction 


    // *0x0($data_ptr_27) = $$28$
    // Spilling destination Deref movl $28$, 0x0($data_ptr_27)
    movl -192(%ebp), %ebx
    // Spilling memory movl $28$, 0x0(94)
    movl -72(%ebp), %eax
    movl %eax, 0x0(%ebx)
    // End spill memory movl $28$, 0x0(94)
    //  end Deref
    // End Instruction 


    // *$26$ = ($$26$ + 3)
    // Spilling memory movl $26$, $26$
    // End spill memory movl $26$, $26$
    addl $3, -44(%ebp)
    // End Instruction 


    // *0x0($data_ptr_25) = $$26$
    // Spilling destination Deref movl $26$, 0x0($data_ptr_25)
    movl -188(%ebp), %eax
    // Spilling memory movl $26$, 0x0(95)
    movl -44(%ebp), %ebx
    movl %ebx, 0x0(%eax)
    // End spill memory movl $26$, 0x0(95)
    //  end Deref
    // End Instruction 


    // *$24$ = ($$24$ + 3)
    // Spilling memory movl $24$, $24$
    // End spill memory movl $24$, $24$
    addl $3, -24(%ebp)
    // End Instruction 


    // *0x0($data_ptr_23) = $$24$
    // Spilling destination Deref movl $24$, 0x0($data_ptr_23)
    movl -184(%ebp), %eax
    // Spilling memory movl $24$, 0x0(97)
    movl -24(%ebp), %ebx
    movl %ebx, 0x0(%eax)
    // End spill memory movl $24$, 0x0(97)
    //  end Deref
    // End Instruction 


    // *$22$ = ($$22$ + 3)
    // Spilling memory movl $22$, $22$
    // End spill memory movl $22$, $22$
    addl $3, -40(%ebp)
    // End Instruction 


    // *0x0($data_ptr_21) = $$22$
    // Spilling destination Deref movl $22$, 0x0($data_ptr_21)
    movl -180(%ebp), %eax
    // Spilling memory movl $22$, 0x0(99)
    movl -40(%ebp), %ebx
    movl %ebx, 0x0(%eax)
    // End spill memory movl $22$, 0x0(99)
    //  end Deref
    // End Instruction 


    // *$20$ = ($$20$ + 3)
    // Spilling memory movl $20$, $20$
    // End spill memory movl $20$, $20$
    addl $3, -88(%ebp)
    // End Instruction 


    // *0x0($data_ptr_19) = $$20$
    // Spilling destination Deref movl $20$, 0x0($data_ptr_19)
    movl -236(%ebp), %eax
    // Spilling memory movl $20$, 0x0(101)
    movl -88(%ebp), %ebx
    movl %ebx, 0x0(%eax)
    // End spill memory movl $20$, 0x0(101)
    //  end Deref
    // End Instruction 


    // *$18$ = ($$18$ + 3)
    // Spilling memory movl $18$, $18$
    // End spill memory movl $18$, $18$
    addl $3, -56(%ebp)
    // End Instruction 


    // *0x0($data_ptr_17) = $$18$
    // Spilling destination Deref movl $18$, 0x0($data_ptr_17)
    movl -232(%ebp), %eax
    // Spilling memory movl $18$, 0x0(103)
    movl -56(%ebp), %ebx
    movl %ebx, 0x0(%eax)
    // End spill memory movl $18$, 0x0(103)
    //  end Deref
    // End Instruction 


    // *$16$ = ($$16$ + 3)
    // Spilling memory movl $16$, $16$
    // End spill memory movl $16$, $16$
    addl $3, -96(%ebp)
    // End Instruction 


    // *0x0($data_ptr_15) = $$16$
    // Spilling destination Deref movl $16$, 0x0($data_ptr_15)
    movl -228(%ebp), %eax
    // Spilling memory movl $16$, 0x0(105)
    movl -96(%ebp), %ebx
    movl %ebx, 0x0(%eax)
    // End spill memory movl $16$, 0x0(105)
    //  end Deref
    // End Instruction 


    // *$14$ = ($$14$ + 3)
    // Spilling memory movl $14$, $14$
    // End spill memory movl $14$, $14$
    addl $3, -32(%ebp)
    // End Instruction 


    // *0x0($data_ptr_13) = $$14$
    // Spilling destination Deref movl $14$, 0x0($data_ptr_13)
    movl -224(%ebp), %ebx
    // Spilling memory movl $14$, 0x0(107)
    movl -32(%ebp), %eax
    movl %eax, 0x0(%ebx)
    // End spill memory movl $14$, 0x0(107)
    //  end Deref
    // End Instruction 


    // *$12$ = ($$12$ + 3)
    // Spilling memory movl $12$, $12$
    // End spill memory movl $12$, $12$
    addl $3, -80(%ebp)
    // End Instruction 


    // *0x0($data_ptr_11) = $$12$
    // Spilling destination Deref movl $12$, 0x0($data_ptr_11)
    movl -220(%ebp), %eax
    // Spilling memory movl $12$, 0x0(109)
    movl -80(%ebp), %ebx
    movl %ebx, 0x0(%eax)
    // End spill memory movl $12$, 0x0(109)
    //  end Deref
    // End Instruction 


    // *$10$ = ($$10$ + 3)
    // Spilling memory movl $10$, $10$
    // End spill memory movl $10$, $10$
    addl $3, -116(%ebp)
    // End Instruction 


    // *0x0($data_ptr_9) = $$10$
    // Spilling destination Deref movl $10$, 0x0($data_ptr_9)
    movl -152(%ebp), %ebx
    // Spilling memory movl $10$, 0x0(111)
    movl -116(%ebp), %eax
    movl %eax, 0x0(%ebx)
    // End spill memory movl $10$, 0x0(111)
    //  end Deref
    // End Instruction 


    // *$8$ = ($$8$ + 3)
    // Spilling memory movl $8$, $8$
    // End spill memory movl $8$, $8$
    addl $3, -48(%ebp)
    // End Instruction 


    // *0x0($data_ptr_7) = $$8$
    // Spilling destination Deref movl $8$, 0x0($data_ptr_7)
    movl -140(%ebp), %eax
    // Spilling memory movl $8$, 0x0(113)
    movl -48(%ebp), %ebx
    movl %ebx, 0x0(%eax)
    // End spill memory movl $8$, 0x0(113)
    //  end Deref
    // End Instruction 


    // *$6$ = ($$6$ + 3)
    // Spilling memory movl $6$, $6$
    // End spill memory movl $6$, $6$
    addl $3, -20(%ebp)
    // End Instruction 


    // *0x0($data_ptr_5) = $$6$
    // Spilling destination Deref movl $6$, 0x0($data_ptr_5)
    movl -136(%ebp), %ebx
    // Spilling memory movl $6$, 0x0(115)
    movl -20(%ebp), %eax
    movl %eax, 0x0(%ebx)
    // End spill memory movl $6$, 0x0(115)
    //  end Deref
    // End Instruction 


    // *$4$ = ($$4$ + 3)
    // Spilling memory movl $4$, $4$
    // End spill memory movl $4$, $4$
    addl $3, -4(%ebp)
    // End Instruction 


    // *0x0($data_ptr_3) = $$4$
    // Spilling destination Deref movl $4$, 0x0($data_ptr_3)
    movl -148(%ebp), %ebx
    // Spilling memory movl $4$, 0x0(117)
    movl -4(%ebp), %eax
    movl %eax, 0x0(%ebx)
    // End spill memory movl $4$, 0x0(117)
    //  end Deref
    // End Instruction 


    // *$2$ = ($$2$ + 3)
    // Spilling memory movl $2$, $2$
    // End spill memory movl $2$, $2$
    addl $3, -112(%ebp)
    // End Instruction 


    // *0x0($data_ptr_1) = $$2$
    // Spilling destination Deref movl $2$, 0x0($data_ptr_1)
    movl -144(%ebp), %eax
    // Spilling memory movl $2$, 0x0(119)
    movl -112(%ebp), %ebx
    movl %ebx, 0x0(%eax)
    // End spill memory movl $2$, 0x0(119)
    //  end Deref
    // End Instruction 


    // *$0$ = ($$0$ + 3)
    // Spilling memory movl $0$, $0$
    // End spill memory movl $0$, $0$
    addl $3, -76(%ebp)
    // End Instruction 


    // *x = $$0$
    movl -76(%ebp), %eax
    // End Instruction 


    // *$64$ = $x#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %eax, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$65$ = $$64$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$66$ = $$65$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$67$ = $$66$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$68$ = $$67$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$69$ = $$68$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$70$ = $$69$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$71$ = $$70$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$72$ = $$71$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$73$ = $$72$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$74$ = $$73$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$75$ = $$74$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$76$ = $$75$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$77$ = $$76$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$78$ = $$77$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$79$ = $$78$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$80$ = $$79$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$81$ = $$80$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$82$ = $$81$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$83$ = $$82$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$84$ = $$83$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$85$ = $$84$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$86$ = $$85$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$87$ = $$86$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$88$ = $$87$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$89$ = $$88$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$90$ = $$89$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$91$ = $$90$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$92$ = $$91$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$93$ = $$92$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$94$ = $$93$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$95$ = $$94$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    // End Instruction 


    // *$96$ = $$95$#0
    subl $20, %esp
    movl %eax, 0x8(%esp)
    movl %ecx, 0xc(%esp)
    movl %edx, 0x10(%esp)
    movl %ebx, (%esp)
    movl $0, 4(%esp)
    call get_subscript
    movl %eax, %ebx
    movl 0x8(%esp), %eax
    movl 0xc(%esp), %ecx
    movl 0x10(%esp), %edx
    addl $20, %esp
    subl $12, %esp
    movl %eax, (%esp)
    movl %ecx, 4(%esp)
    movl %edx, 8(%esp)
    pushl %ebx
    call print_any
    movl 4(%esp), %eax
    movl 8(%esp), %ecx
    movl 12(%esp), %edx
    addl $16, %esp
    movl $0, %eax
    leave
    ret
