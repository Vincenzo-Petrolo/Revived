test:
	@cd c_codes && riscv32-unknown-elf-gcc -S -ffixed-t3 simple.c && mv simple.s ../riscv_asm
assemble:
	@cd dlx_asm && ./assembler.sh simple.s