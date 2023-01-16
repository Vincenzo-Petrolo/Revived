main:
	addi	r2,r2,#-32
	sw	28(r2),r1
	sw	24(r2),r8
	addi	r8,r2,#32
	addi	r15,#1,#0
	sw	-24(r8),r15
	addi	r15,#2,#0
	sw	-28(r8),r15
	lw	r14,-24(r8)
	addi	r15,#1,#0
	lw	r11,-28(r8)
	addi	r10,#1,#0
	jal	add
	sw	-32(r8),r10
L2:
	sw	-20(r8),r0
	j	.L3
L4:
	lw	r11,-20(r8)
	lw	r10,-24(r8)
	jal	add
	sw	-32(r8),r10
	lw	r15,-20(r8)
	addi	r15,r15,#1
	sw	-20(r8),r15
L3:
	lw	r14,-20(r8)
	addi	r15,#9,#0
	lw	r11,-28(r8)
	lw	r10,-24(r8)
	jal	add
	sw	-32(r8),r10
	lw	r15,-32(r8)
	addi	r10,r15,#0
	lw	r1,28(r2)
	lw	r8,24(r2)
	addi	r2,r2,#32
	jr	r1
add:
	addi	r2,r2,#-32
	sw	28(r2),r8
	addi	r8,r2,#32
	sw	-20(r8),r10
	sw	-24(r8),r11
	lw	r14,-20(r8)
	lw	r15,-24(r8)
	add	r15,r14,r15
	addi	r10,r15,#0
	lw	r8,28(r2)
	addi	r2,r2,#32
	jr	r1
