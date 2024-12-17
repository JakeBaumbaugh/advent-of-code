import re

with open('input.txt', 'r') as file:
    lines = file.readlines()

registers = {'a': 1, 'b': 0, 'step': 0}

def hlf(register, num):
    registers[register] /= 2
    registers['step'] += 1
def tpl(register, num):
    registers[register] *= 3
    registers['step'] += 1
def inc(register, num):
    registers[register] += 1
    registers['step'] += 1
def jmp(register, num):
    registers['step'] += num
def jie(register, num):
    if registers[register] % 2 == 0:
        registers['step'] += num
    else:
        registers['step'] += 1
def jio(register, num):
    if registers[register] == 1:
        registers['step'] += num
    else:
        registers['step'] += 1

instruction_map = {'hlf': hlf, 'tpl': tpl, 'inc': inc, 'jmp': jmp, 'jie': jie, 'jio': jio}
instructions = []

def parse_instruction(line):
    match = re.search('(\w+) (\w)?,? ?([+-]\d+)?', line)
    instr = match.group(1)
    register = match.group(2)
    num = match.group(3)
    instructions.append({'instr': instr, 'register': register, 'num': None if num is None else int(num)})

def state():
    return ', '.join([k + ':' + str(registers[k]) for k in registers])

for line in lines:
    parse_instruction(line)

prev_states = set()
while registers['step'] < len(instructions):
    print(registers)
    reg_state = state()
    if reg_state in prev_states:
        raise Exception('duplicate state ' + reg_state)
    else:
        prev_states.add(reg_state)
    instruction = instructions[registers['step']]
    print(instruction)
    instruction_map[instruction['instr']](instruction['register'], instruction['num'])

for key in registers:
    print(key, ':', registers[key])