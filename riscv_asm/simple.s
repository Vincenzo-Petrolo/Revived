	.file	"simple.c"
	.option nopic
	.attribute arch, "rv32i2p0"
	.attribute unaligned_access, 0
	.attribute stack_align, 16
	.text
	.align	2
	.globl	main
	.type	main, @function
main:
	addi	sp,sp,-32
	sw	ra,28(sp)
	sw	s0,24(sp)
	addi	s0,sp,32
	li	a5,1
	sw	a5,-24(s0)
	li	a5,2
	sw	a5,-28(s0)
	lw	a4,-24(s0)
	li	a5,1
	bne	a4,a5,.L2
	lw	a1,-28(s0)
	li	a0,1
	call	add
	sw	a0,-32(s0)
.L2:
	sw	zero,-20(s0)
	j	.L3
.L4:
	lw	a1,-20(s0)
	lw	a0,-24(s0)
	call	add
	sw	a0,-32(s0)
	lw	a5,-20(s0)
	addi	a5,a5,1
	sw	a5,-20(s0)
.L3:
	lw	a4,-20(s0)
	li	a5,9
	ble	a4,a5,.L4
	lw	a1,-28(s0)
	lw	a0,-24(s0)
	call	add
	sw	a0,-32(s0)
	lw	a5,-32(s0)
	mv	a0,a5
	lw	ra,28(sp)
	lw	s0,24(sp)
	addi	sp,sp,32
	jr	ra
	.size	main, .-main
	.align	2
	.globl	add
	.type	add, @function
add:
	addi	sp,sp,-32
	sw	s0,28(sp)
	addi	s0,sp,32
	sw	a0,-20(s0)
	sw	a1,-24(s0)
	lw	a4,-20(s0)
	lw	a5,-24(s0)
	add	a5,a4,a5
	mv	a0,a5
	lw	s0,28(sp)
	addi	sp,sp,32
	jr	ra
	.size	add, .-add
	.ident	"GCC: (g2ee5e430018) 12.2.0"
