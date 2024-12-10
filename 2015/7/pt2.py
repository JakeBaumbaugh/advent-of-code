import re

with open('input.txt', 'r') as file:
    lines = file.readlines()

class Gate:
    def __init__(self, instr, in1, in2, out):
        self.instr = instr
        self.in1 = in1
        self.in2 = in2
        self.out = out

def parse_gate(line):
    match = re.search('^([a-z]+|\d+) -> (\w+)$', line)
    if match is not None:
        return Gate('ASSIGN', match.group(1), None, match.group(2))
    else:
        match = re.search('([a-z]+|\d+)? ?([A-Z]+) ([a-z]+|\d+) -> (\w+)', line)
        return Gate(match.group(2), match.group(1), match.group(3), match.group(4))

gates = [parse_gate(line) for line in lines]
gate_dict = {gate.out : gate for gate in gates}
wire_dict = {}

def calc_wire(wire):
    print('calculating wire', wire)
    if wire not in gate_dict:
        raise "unknown wire " + wire
    
    def value(text: str):
        if text.isdecimal():
            return int(text)
        elif text in wire_dict:
            return wire_dict[text]
        else:
            return calc_wire(text)

    gate = gate_dict[wire]
    if gate.instr == 'ASSIGN':
        wire_value = value(gate.in1)
    elif gate.instr == 'NOT':
        wire_value = ~value(gate.in2)
    elif gate.instr == 'AND':
        wire_value = value(gate.in1) & value(gate.in2)
    elif gate.instr == 'OR':
        wire_value = value(gate.in1) | value(gate.in2)
    elif gate.instr == 'LSHIFT':
        wire_value = value(gate.in1) << value(gate.in2)
    elif gate.instr == 'RSHIFT':
        wire_value = value(gate.in1) >> value(gate.in2)
    else:
        raise "unknown instr " + gate.instr
    wire_dict[wire] = wire_value
    return wire_value

orig_a = calc_wire('a')
gate_dict['b'].in1 = str(orig_a)
wire_dict = {}
print(calc_wire('a'))