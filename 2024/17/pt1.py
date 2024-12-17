registers = {'A': 55593699, 'B': 0, 'C': 0, 'step': 0}
program = [2,4,1,3,7,5,0,3,1,5,4,4,5,5,3,0]
output = ''

def combo(operand):
    if operand >= 0 and operand <= 3:
        return operand
    if operand == 4:
        return registers['A']
    if operand == 5:
        return registers['B']
    if operand == 6:
        return registers['C']
    if operand == 7:
        raise Exception('operand 7')
def step():
    registers['step'] += 2

def adv(operand):
    registers['A'] //= 2**combo(operand)
    step()
def bxl(operand):
    registers['B'] ^= operand
    step()
def bst(operand):
    registers['B'] = combo(operand) % 8
    step()
def jnz(operand):
    if registers['A'] != 0:
        registers['step'] = operand
    else:
        step()
def bxc(operand):
    registers['B'] ^= registers['C']
    step()
def out(operand):
    global output
    output += str(combo(operand) % 8) + ','
    step()
def bdv(operand):
    registers['B'] = registers['A'] // 2**combo(operand)
    step()
def cdv(operand):
    registers['C'] = registers['A'] // 2**combo(operand)
    step()

instruction_map = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

prev_states = set()
while registers['step'] + 1 < len(program):
    instr = program[registers['step']]
    operand = program[registers['step'] + 1]
    instruction_map[instr](operand)

for key in registers:
    print(key, ':', registers[key])
print('output:', output[:-1])