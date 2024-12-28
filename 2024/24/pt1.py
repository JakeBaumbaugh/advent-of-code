import re

with open('input.txt', 'r') as file:
    lines = file.readlines()

class Gate:
    def __init__(self, instr, in1, in2, out):
        self.instr = instr
        self.in1 = in1
        self.in2 = in2
        self.out = out

def parse_gate(line: str):
    if len(line.strip()) == 0:
        return None
    match = re.search('^([a-z0-9]+): (\d)$', line)
    if match is not None:
        return Gate('ASSIGN', match.group(2), None, match.group(1))
    else:
        match = re.search('([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)', line)
        return Gate(match.group(2), match.group(1), match.group(3), match.group(4))

gates = [parse_gate(line) for line in lines]
gate_dict = {gate.out : gate for gate in gates if gate is not None}
wire_dict = {}

def calc_wire(wire):
    # print('calculating wire', wire)
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
    elif gate.instr == 'AND':
        wire_value = 1 if value(gate.in1) == 1 and value(gate.in2) == 1 else 0
    elif gate.instr == 'OR':
        wire_value = min(value(gate.in1) + value(gate.in2), 1)
    elif gate.instr == 'XOR':
        wire_value = (value(gate.in1) + value(gate.in2)) % 2
    else:
        raise "unknown instr " + gate.instr
    wire_dict[wire] = wire_value
    return wire_value


x_wires = [k for k in gate_dict if k.startswith('x')]
y_wires = [k for k in gate_dict if k.startswith('y')]
z_wires = [k for k in gate_dict if k.startswith('z')]
x = 0
for wire in x_wires:
    if calc_wire(wire) == 1:
        exp = int(wire[1:])
        x += 2**exp
print(x)
y = 0
for wire in y_wires:
    if calc_wire(wire) == 1:
        exp = int(wire[1:])
        y += 2**exp
print(y)
print(x + y)
z = 0
for wire in z_wires:
    if calc_wire(wire) == 1:
        exp = int(wire[1:])
        z += 2**exp
print(z)

x_wires.sort(reverse=True)
y_wires.sort(reverse=True)
z_wires.sort(reverse=True)
print('', ''.join(str(calc_wire(wire)) for wire in x_wires))
print('', ''.join(str(calc_wire(wire)) for wire in y_wires))
print(''.join(str(calc_wire(wire)) for wire in z_wires))