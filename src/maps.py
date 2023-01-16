"""
Useful maps for converting from risc to dlx
"""

regs_map = {
    "zero"  :   "r0",
    "0"     :   "r0",   # has two names in ABI
    "ra"    :   "r31",
    "sp"    :   "r2",
    "gp"    :   "r3",
    "tp"    :   "r4",
    "t0"    :   "r5",
    "t1"    :   "r6",
    "t2"    :   "r7",
    "s0"    :   "r8",
    "fp"    :   "r8",   # has two names in ABI
    "s1"    :   "r9",
    "a0"    :   "r10",
    "a1"    :   "r11",
    "a2"    :   "r12",
    "a3"    :   "r13",
    "a4"    :   "r14",
    "a5"    :   "r15",
    "a6"    :   "r16",
    "a7"    :   "r17",
    "s2"    :   "r18",
    "s3"    :   "r19",
    "s4"    :   "r20",
    "s5"    :   "r21",
    "s6"    :   "r22",
    "s7"    :   "r23",
    "s8"    :   "r24",
    "s9"    :   "r25",
    "s10"   :   "r26",
    "s11"   :   "r27",
    "t3"    :   "r28",  # t3 aka r28 is used when converting complex branch instructions, it's never used by the compiler
    "t4"    :   "r29",
    "t5"    :   "r30",
    "t6"    :   "r1"
}

pseudo_map = {
    "li"    :   "addi",
    "mv"    :   "addi",
    "not"   :   "xori",
    "neg"   :   "sub",
    "call"  :   "jal",
    "jr"    :   "jr",
    "bne"   :   "sne",
    "beq"   :   "seq",
    "ble"   :   "sle",
    "bge"   :   "sge",
    "blt"   :   "slt",
    "bgt"   :   "sgt"
}

"""
Instructions that we didn't implement in DLX and are present in RISC-V are
implemented by means of procedures.
"""