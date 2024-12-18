from math import floor
from collections import defaultdict

input_ = open("data/day17.txt", "r").read().splitlines()

registerA = int(input_[0].split(": ")[1])
registerB = int(input_[1].split(": ")[1])
registerC = int(input_[2].split(": ")[1])

registers = {"A": registerA, "B": registerB, "C": registerC}
original_registers = registers.copy()

program = list(map(int,input_[4].split(": ")[1].split(",")))

combo_map = {0:lambda:0,1:lambda:1,2:lambda:2,3:lambda:3,4:lambda:registers["A"],5:lambda:registers["B"],6:lambda:registers["C"]}

instruction_pointer = 0

def adv(operand): #0
    combo = combo_map[operand]()
    registers["A"] = floor(registers["A"] / (2 ** combo))
    
def bxl(operand): #1
    registers["B"] = registers["B"] ^ operand
    
def bst(operand): #2
    combo = combo_map[operand]()
    registers["B"] = combo % 8

def jnz(operand): #3
    global instruction_pointer
    if registers["A"] !=0:
        instruction_pointer = operand - 2
        
def bxc(operand): #4
    registers["B"] = registers["B"] ^ registers["C"]
    
def out(operand): #5
    combo = combo_map[operand]()
    return combo % 8

def bdv(operand): #6
    combo = combo_map[operand]()
    registers["B"] = floor(registers["A"] / (2 ** combo))
    
def cdv(operand): #7
    combo = combo_map[operand]()
    registers["C"] = floor(registers["A"] / (2 ** combo))
    
instruction_map = {0: lambda x: adv(x), 1: lambda x: bxl(x), 2: lambda x: bst(x), 3: lambda x: jnz(x), 4: lambda x: bxc(x), 5: lambda x: out(x), 6: lambda x: bdv(x), 7: lambda x: cdv(x)}

def run_check():
    global instruction_pointer
    instruction_pointer = 0
    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer+1]
        out_ =  instruction_map[opcode](operand)
        #print(opcode,operand,[(x,"{0:b}".format(y)) for x,y in registers.items()],"out:",out_)
        if out_ is not None:
            yield str(out_)
        instruction_pointer += 2

pt1 = ""  
for x in run_check():
    pt1 += x

print("pt1",",".join(pt1))

bytes_set = defaultdict(set)
bytes_set[1] = {"1"}
for target_length in range(1,len(program)+1):

    candidates = set()
    options = bytes_set[target_length].copy()
    for starting_bin in options:
        print("TARGET LENGTH:",target_length,"NEW STARTING BIN --- ",starting_bin)
        found=False
        starting_point = int("1" + starting_bin.zfill(42),2)
        registerA = starting_point
        last_found = 0
        new_step = 2**len(starting_bin)
        z = 0
        while registerA > 0 and not found and z < 100000:
            found=True
            found_length = 0
            registers = original_registers.copy()
            match_ = (str(x) for x in program)
            registers["A"] = registerA
            
            for ix,x in enumerate(run_check()):
                try:
                    if x != next(match_):
                        found=False
                        break
                    else:
                        current_ = "{0:b}".format(registers["A"])
                        found_length += 1
                except:
                    found=False
                    break
                
            if found_length >= target_length:

                initial = "{0:b}".format(registerA)
                current = initial[len(current_):]
                
                last_found=found_length
                if current not in bytes_set.get(found_length,set()):
                    bytes_set[found_length].add(current)
                stop_here = 1
            
            if found:
                candidates.add(registerA)
                
            registerA += new_step
            z+=1
            
print(list(sorted(candidates)))

  


        