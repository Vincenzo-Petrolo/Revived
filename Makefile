test:
	@cd c_codes && riscv32-unknown-elf-gcc -S simple.c && mv simple.s ../riscv_asm