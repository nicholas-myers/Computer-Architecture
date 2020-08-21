"""CPU functionality."""

import sys

ops = {
    0b10100000: "ADD",
    0b10101000: "AND",
    0b01010000: "CALL",
    0b10100111: "CMP",
    0b00000001: "HLT",
    0b01010101: "JEQ",
    0b01010100: "JMP",
    0b01010110: "JNE",
    0b10000010: "LDI",
    0b10100010: "MUL",
    0b01000110: "POP",
    0b01001000: "PRA",
    0b01000111: "PRN",
    0b01000101: "PUSH",
    0b00010001: "RET",
    0b10000100: "ST"
}

alus = {
    0b10100000: "ADD",
    0b10101000: "AND",
    0b10100010: "MUL"
}

# Flag
FL = [0] * 3
# Stack Pointer
SP = 7
# interrupt mask
IM = 5
# Interrupt status
IS = 6
INT = [0] * 8

class CPU:
    """Main CPU class."""
    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8
        self.reg[SP] = 0xf4
        self.ram = [0] * 256
        self.pc = 0
        self.running = False
        
    def load(self):
        """Load a program into memory."""
        address = 0
        # take in a file, read the file
        if len(sys.argv) != 2:
            print(sys.argv)
            print("usage: ls8.py examples/filename")
            sys.exit(1)
        try: 
            with open(sys.argv[1]) as f:
                for line in f:
                    line = line.strip()
                    temp = line.split()
                    if len(temp) == 0:
                        continue
                    if temp[0][0] == "#":
                        continue
                    try:
                        num = temp[0]
                        bin_num = 0
                        place = 128
                        # convert the number to its decimal version
                        for n in num:
                            bin_num += (int(n) * place)
                            place = int(place / 2)
                        
                        self.ram[address] = bin_num
                        address +=1
                        # print(self.ram)
                    except ValueError:
                        print(f"Invalid Number: {temp[0]}")
                        sys.exit(1)
        except FileNotFoundError:
            print(f"Couldn't open {sys.argv[1]}")
        if address == 0:
            print("program was Empty!")

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        # print(reg_a, reg_b)
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        if op == "AND":
            # BITWISE _ AND rega and reg b
            # store in rega
            num1 = int(self.reg[reg_a])
            print(num1)
            print(bin(num1))
            num2 = int(self.reg[reg_b])
            print(num2)
            print(bin(num2))
            res = bin(num1 & num2)
            print(res)
        if op == "CMP":
            if self.reg[reg_a] == self.reg[reg_b]:
                # set FL from E to 1
                FL[-1] = 1
            else:
                # other wise set to 0
                FL[-1] = 0
            
            if self.reg[reg_a] > self.reg[reg_b]:
                # set FL from G to 1
                FL[-2] = 1
            else:
                # otherwise to 0
                FL[-2] = 0
                
            if self.reg[reg_a] < self.reg[reg_b]:
                # set FL bit from L to 1
                FL[-3] = 1
            else:
                # otherwise set to 0
                FL[-3] = 0
            
        if op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        # else:
        #     raise Exception("Unsupported ALU operation")
    
    # ram functions
    def ram_read(self, MAR):
        # print(self.ram[MAR])
        return self.ram[MAR]
    
    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR
        
    # OP functions
    def add_alu(self, reg_a, reg_b):
        self.reg[reg_a] += self.reg[reg_b]
        self.pc += 3
    
    def and_alu(self, reg_a, reg_b):
        num1 = int(self.reg[reg_a])
        print(num1)
        print(bin(num1))
        num2 = int(self.reg[reg_b])
        print(num2)
        print(bin(num2))
        res = bin(num1 & num2)
        print(res)
        self.pc += 3
    
    def call(self, reg_num):
        # print("this happened")
        # print(self.pc)
        ret_addr = self.pc + 2
        self.reg[SP] -= 1
        self.ram[self.reg[SP]] = ret_addr
        # print(self.ram[self.reg[SP]])
        self.pc = self.reg[arg1]    
    
    def cmp_alu(self, reg_a, reg_b):
        if self.reg[reg_a] == self.reg[reg_b]:
            # set FL from E to 1
            FL[-1] = 1
        else:
            # other wise set to 0
            FL[-1] = 0
            
        if self.reg[reg_a] > self.reg[reg_b]:
                # set FL from G to 1
                FL[-2] = 1
        else:
            # otherwise to 0
            FL[-2] = 0
                            
        if self.reg[reg_a] < self.reg[reg_b]:
            # set FL bit from L to 1
            FL[-3] = 1
        else:
            # otherwise set to 0
            FL[-3] = 0
        self.pc += 3
    
    def hlt(self):
        self.running = False
    
    def jeq(self, reg_num):
        if int(FL[-1]) == 1:
            self.pc = self.reg[reg_num]
        else:
            self.pc += 2
    
    def jump(self, reg_num):
        self.pc = self.reg[reg_num] 
    
    def jne(self, reg_num):
        if int(FL[-1]) == 0:
            self.pc = self.reg[reg_num]
        else:
            self.pc += 2
    def ldi(self, reg_num, value):
        self.reg[reg_num] = value
        self.pc += 3

    def mul_alu(self, reg_a, reg_b):
        self.reg[reg_a] *= self.reg[reg_b]

    def pra(self, reg_num):
        print(self.reg[reg_num])
        self.pc += 2
    
    def prn(self, reg_num):
        print(self.reg[reg_num])
        self.pc += 2
        
    def push_reg(self, reg_num):
        self.reg[SP] -= 1
        stack_top = self.reg[SP]
        self.ram[stack_top] = self.reg[reg_num]
        self.pc += 2
    
    def pop_reg(self, reg_num):
        stack_top = self.reg[SP]
        self.reg[reg_num] = self.ram[stack_top]
        self.reg[SP] += 1
        # print(f"stack: {self.ram[0xE4:0xF4]}")
        self.pc += 2
    
    def ret_sub(self):
        # print("this happened")
        ret_addr = self.ram[self.reg[SP]]
        # print(ret_addr)
        self.reg[SP] += 1
        self.pc = ret_addr
    
    
    
    def run(self):
        """Run the CPU."""
        # self.trace()
        # start running
        self.running = True
        
        LDI = 0b10000010
        PRN = 0b01000111
        HLT = 0b00000001
        MUL = 0b10100010
        PUSH = 0b01000101
        POP = 0b01000110
        CALL = 0b01010000
        ADD = 0b10100000
        RET = 0b00010001
        JMP = 0b01010100
        CMP = 0b10100111
        JEQ = 0b01010101
        JNE = 0b01010110
        ST = 0b10000100
        PRA = 0b01001000
        AND = 0b10101000
        
        while self.running:
            # get the instruction from ram
            ir = self.ram_read(self.pc)
            arg1 = self.ram_read(self.pc + 1)
            arg2 = self.ram_read(self.pc + 2)
            # print(ir)
            if ir == LDI:
                self.reg[arg1] = arg2
                self.pc += 3
            if ir == PRN:
                print(self.reg[arg1])
                self.pc += 2
            if ir == HLT:
                self.running = False
            if ir == ADD:
                self.alu("ADD", arg1, arg2)
                self.pc+=3
            if ir == MUL:
                self.alu("MUL", arg1, arg2)
                # print(multiply)
                self.pc += 3
            if ir == PUSH:
                self.reg[SP] -= 1
                stack_top = self.reg[SP]
                self.ram[stack_top] = self.reg[arg1]
                self.pc += 2
                # print(f"stack: {self.ram[0xE4:0xF4]}")
            if ir == POP:
                stack_top = self.reg[SP]
                self.reg[arg1] = self.ram[stack_top]
                self.reg[SP] += 1
                # print(f"stack: {self.ram[0xE4:0xF4]}")
                self.pc += 2
            if ir == CALL:
                # print("this happened")
                # print(self.pc)
                ret_addr = self.pc + 2
                self.reg[SP] -= 1
                self.ram[self.reg[SP]] = ret_addr
                # print(self.ram[self.reg[SP]])
                self.pc = self.reg[arg1]
            if ir == RET:
                # print("this happened")
                ret_addr = self.ram[self.reg[SP]]
                # print(ret_addr)
                self.reg[SP] += 1
                self.pc = ret_addr
            if ir == JMP:
                self.pc = self.reg[arg1]          
            if ir == CMP:
                self.alu("CMP", arg1, arg2)
                self.pc += 3
            if ir == JNE:
                if int(FL[-1]) == 0:
                    self.pc = self.reg[arg1]
                else:
                    self.pc += 2
            if ir == JEQ:
                if int(FL[-1]) == 1:
                    self.pc = self.reg[arg1]
                else:
                    self.pc += 2
            if ir == ST:
                addr = self.reg[arg1]
                value = self.reg[arg2]
                self.ram_write(addr, value)
                self.pc += 3
            if ir == PRA:
                print(self.reg[arg1])
                self.pc += 2
            if ir == AND:
                self.alu("AND", arg1, arg2)
                self.pc += 3
    
    # def run(self):
    #     self.running = True

    #     while self.running:
    #         IR = self.ram_read(self.pc)
    #         arg1 = self.ram_read(self.pc + 1)
    #         arg2 = self.ram_read(self.pc + 2)
            
    #         ops = {
    #             0b10100000: self.add_alu(arg1, arg2),
    #             0b10101000: self.and_alu(arg1, arg2),
    #             0b01010000: self.call(arg1),
    #             0b10100111: self.cmp_alu(arg1, arg2),
    #             0b00000001: self.hlt(),
    #             0b01010101: self.jeq(arg1),
    #             0b01010100: self.jump(arg1),
    #             0b01010110: self.jne(arg1),
    #             0b10000010: self.ldi(arg1, arg2),
    #             0b10100010: self.mul_alu(arg1, arg2),
    #             0b01000110: self.pop(arg1),
    #             0b01001000: self.pra(arg1),
    #             0b01000111: self.prn(arg1),
    #             0b01000101: self.push(arg1),
    #             0b00010001: self.ret_sub(),
    #             0b10000100: "ST"
    #         }
            
    #         ops[IR]