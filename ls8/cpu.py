"""CPU functionality."""

import sys


LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001
class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8
        self.ram = [0] * 256
        self.pc = 0

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            # instruction LDI
            0b10000010, # LDI R0,8
            # register position
            0b00000000,
            # the value we want to put in that position
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def ram_read(self, MAR):
        # print(self.ram[MAR])
        return self.ram[MAR]
    
    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR
        
    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        # self.trace()
        # start running
        running = True
        
        
        while running:
            # get the instruction from ram
            
            ir = self.ram_read(self.pc)
            arg1 = self.pc + 1
            arg2 = self.pc + 2
            # print(ir)
            if ir == LDI:
                # print(self.pc + 1)
                # break
                self.reg[self.ram_read(arg1)] = self.ram_read(arg2)
                self.pc += 3
            if ir == PRN:
                print(self.reg[self.ram_read(arg1)])
                self.pc += 2
            if ir == HLT:
                running = False