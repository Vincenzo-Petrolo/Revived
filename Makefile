test:
	@cd c_codes && riscv32-unknown-elf-gcc -S simple.c && mv simple.s ../riscv_asm
assemble:
	@cd dlx_asm && ./assembler.sh simple.s