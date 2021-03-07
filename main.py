from disassembler import *


# load prg
bytes = load_file("s3.prg")

# turn bytes into asm code
startaddr = 4096
assembly = bytes_to_asm(bytes, startaddr, opcodes)

# convert it into a readable format
display_full_assembly(assembly)

program = create_program(assembly)

# save as file
write_asm_file("output.asm", program)


print("\n")
num = 255
num2 = 32
shifted = hex((num << 8) + num2)[2:]
print(shifted)
