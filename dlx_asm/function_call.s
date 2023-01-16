	addi	r2,r0,#2047
	nop	
	nop	
	nop	
main:
	addi	r2,r2,#-48
	nop	
	nop	
	nop	
	sw	44(r2),r1
	sw	40(r2),r8
	addi	r8,r2,#48
	nop	
	nop	
	addi	r15,#1,#0
	nop	
	nop	
	nop	
	sw	-20(r8),r15
	addi	r15,#2,#0
	nop	
	nop	
	nop	
	sw	-24(r8),r15
	lw	r11,-24(r8)
	lw	r10,-20(r8)
	nop	
	nop	
	jal	add
	nop	
	nop	
	sw	-28(r8),r10
	lw	r11,-24(r8)
	lw	r10,-20(r8)
	nop	
	nop	
	jal	sub
	nop	
	nop	
	sw	-32(r8),r10
	lw	r11,-24(r8)
	lw	r10,-20(r8)
	nop	
	nop	
	jal	mul
	nop	
	nop	
	sw	-36(r8),r10
	addi	r15,#0,#0
	nop	
	nop	
	nop	
	addi	r10,r15,#0
	lw	r1,44(r2)
	lw	r8,40(r2)
	addi	r2,r2,#48
	nop	
	nop	
	jr	r31
	nop	
	nop	
add:
	addi	r2,r2,#-32
	nop	
	nop	
	nop	
	sw	28(r2),r8
	addi	r8,r2,#32
	nop	
	nop	
	nop	
	sw	-20(r8),r10
	sw	-24(r8),r11
	lw	r14,-20(r8)
	nop	
	nop	
	lw	r15,-24(r8)
	nop	
	nop	
	nop	
	add	r15,r14,r15
	nop	
	nop	
	nop	
	addi	r10,r15,#0
	lw	r8,28(r2)
	addi	r2,r2,#32
	nop	
	nop	
	jr	r31
	nop	
	nop	
sub:
	addi	r2,r2,#-32
	nop	
	nop	
	nop	
	sw	28(r2),r8
	addi	r8,r2,#32
	nop	
	nop	
	nop	
	sw	-20(r8),r10
	sw	-24(r8),r11
	lw	r14,-20(r8)
	nop	
	nop	
	lw	r15,-24(r8)
	nop	
	nop	
	nop	
	sub	r15,r14,r15
	nop	
	nop	
	nop	
	addi	r10,r15,#0
	lw	r8,28(r2)
	addi	r2,r2,#32
	nop	
	nop	
	jr	r31
	nop	
	nop	
mul:
	addi	r2,r2,#-48
	nop	
	nop	
	nop	
	sw	44(r2),r1
	sw	40(r2),r8
	addi	r8,r2,#48
	nop	
	nop	
	nop	
	sw	-36(r8),r10
	sw	-40(r8),r11
	sw	-20(r8),r0
	sw	-24(r8),r0
	j	L8
	nop	
	nop	
L9:
	lw	r11,-20(r8)
	lw	r10,-36(r8)
	nop	
	nop	
	jal	add
	nop	
	nop	
	sw	-20(r8),r10
	lw	r15,-24(r8)
	nop	
	nop	
	nop	
	addi	r15,r15,#1
	nop	
	nop	
	nop	
	sw	-24(r8),r15
L8:
	lw	r14,-24(r8)
	nop	
	nop	
	lw	r15,-40(r8)
	nop	
	nop	
	nop	
	slt	r28,r14,r15
	bnez	r28,L9
	nop	
	nop	
	lw	r15,-20(r8)
	nop	
	nop	
	nop	
	addi	r10,r15,#0
	lw	r1,44(r2)
	lw	r8,40(r2)
	addi	r2,r2,#48
	jr	r31
	nop	
	nop	
