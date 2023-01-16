# ReViveD: Risc-V to Dlx toolchain

Given that last GCC compiler for DLX architecture has been lost (thus the name of this project :-) , my aim is to bring a new way of cross-compiling C codes for DLX passing through RISC-V cross-compiler.

## Compiling C codes
```bash
riscv32-unknown-elf-gcc -S -ffixed-t3 <some_code.c>
```

## Running the tool
The input assembly file should be RISC-V assembly file obtained by cross-compilation using gcc cross-compiler.

```bash
python3 revived.py --input=<file.s> [--output=<output.s>]
```

## Compiling the DLX assembly
Move into the dlx_asm directory and run the assembler.

```bash
./assembler.sh <code.s>
```