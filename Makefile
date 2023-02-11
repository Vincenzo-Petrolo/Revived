test:
	@cd c_codes && riscv32-unknown-elf-gcc -S -ffixed-t3 sorting_test.c && mv sorting_test.s ../riscv_asm
assemble:
	@cd dlx_asm && ./assembler.sh simple.s