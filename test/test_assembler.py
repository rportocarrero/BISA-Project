# This file contains unit tests for the python assembler
import pytest
import sys
# add source path
sys.path.append('../src')
import assembler

# basic sanity test
def test_sanity():
        assert True

# test missing asembly file
def test_missing_assembly_file():
        with pytest.raises(FileNotFoundError):
            assembler.assemble("","missingFile.as", "")

# test assembly file read
def test_read_assembly_file():
       result = assembler.read_assembly_file("TestFile1.as")
       assert result == ["TEST"]

# test loading ISA description
def test_load_isa_description():
       result = assembler.load_isa_description("BISATest1.json")
       assert result == {'instructions': [{'name': 'NOP', 'opcode': '0x00', 'operands': []}], 'operand-types': {'rd': {'type': 'register', 'bits': 4, 'shift': 8}}}
       
# test tokenization function
def test_tokenization():
       result = assembler.tokenize_lines("ADD R1, R2, R3;")
       assert result == ['ADD', 'R1', 'R2', 'R3;']

# test first pass of compiler on each instruction
def test_first_pass():
       file_lines = assembler.read_assembly_file("TestFile2.as")
       result = assembler.first_pass(file_lines)
       assert result == {'sym1': 0,'sym2': 2}

# test assemble instructions method


# test second pass of compiler
def test_second_pass():
       file_lines = assembler.read_assembly_file("TestFile2.as")
       sym_table = assembler.first_pass(file_lines)
       result = assembler.second_pass(file_lines, sym_table)
       assert result == {'sym1': 0,'sym2': 2}
