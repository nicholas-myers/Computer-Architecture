# +-----16
# |+----8
# ||+---4
# |||+--2
# ||||+-1
# |||||
# 11011 

# 1*16 + 1*8 + 0*4 + 1*2 + 1*1 = 27

# can be split into 4 bits
# convert
# concat to final result

# 0b 0110 0111 
#     6    7
# 0x67

memory = [
    1,
    3, # save_reg r4 37 , the instruction/function
    4, # the register we want to access
    37, #THE VALUE
    4, #new operation
    4, # the register to access
    2
]

registers = [0] * 8
print(registers)

running = True
pc = 0

while running:
    ir = memory[pc] #instruction register
    if ir == 1:
        print("Nick")
        pc+=1
    elif ir == 2:
        running = False
        # pc = 0
    elif ir == 3:
        reg_num = memory[pc +1]
        value = memory[pc + 2]
        registers[reg_num] = value
        print(f"{registers[reg_num]}")
        pc+=3
    elif ir == 4:
        reg_num = memory[pc + 1]
        print(registers[reg_num])
        pc += 2