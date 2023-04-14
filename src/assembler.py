import sys
import json
import re

# This function reads lines from the input assembly file
def read_assembly_file(as_file):
    with open(as_file, 'r') as f:
        lines = f.readlines()
    f.close()
    return lines

# This function loads the isa description from the json file
def load_isa_description(isa_des):
    with open(isa_des, 'r') as f:
        isa_description = json.load(f)
    return isa_description

# This function extracts tokens from lines
def tokenize_lines(line):
    line = line.strip()
    tokens = re.split(r'[,\s]+', line)
    return [t for t in tokens if t]

# This first pass of the assembler builds the symbol table from the tokens.
def first_pass(lines):
    symbol_table = {}
    addr = 0
    for line in lines:
        tokens = tokenize_lines(line)
        if not tokens:
            continue

        if tokens[0].endswith(':'):
            symbol = tokens[0][:-1]
            symbol_table[symbol] = addr
        else:
            addr += 2
    return symbol_table

# this function performs the second pass of the assembler
def second_pass(lines, symbol_table):
    assembled = []

    def assemble_operand(operand):
        if operand.startswith('R'):
            return int(operand[1:])
        elif operand in symbol_table:
            return symbol_table[operand]
        else:
            return int(operand)

    for line in lines:
        tokens = tokenize_lines(line)
        if not tokens or tokens[0].endswith(':'):
            continue

        opcode = tokens[0].upper()
        operands = [assemble_operand(op) for op in tokens[1:]]
        instruction = assemble_instruction(opcode, operands)
        assembled.append(instruction)

    return assembled

# This function assembles the binary
def assemble(bin_file, as_file, isa_des):
    lines = read_assembly_file(as_file)
    isa_description = load_isa_description(isa_des)
    symbol_table = first_pass(lines)
    return

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python assember <binary output file> <assembly file> <isa description json file>")

        bin_file = sys.argv[1]
        as_file = sys.argv[2]
        isa_des = sys.argv[3]

    assemble(bin_file, as_file, isa_des)