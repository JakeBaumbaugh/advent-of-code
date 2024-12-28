import re

with open('input.txt', 'r') as file:
    lines = file.readlines()

class Gate:
    def __init__(self, instr, in1, in2, out):
        self.instr = instr
        self.in1 = in1
        self.in2 = in2
        self.out = out
    
    def has_input(self, in1):
        return self.in1 == in1 or self.in2 == in1

    def has_inputs(self, in1, in2):
        return (self.in1 == in1 and self.in2 == in2) or (self.in2 == in1 and self.in1 == in2)
    
    def get_other_input(self, in1):
        return self.in2 if self.in1 == in1 else self.in1
    
    def __str__(self):
        return f'{self.in1} {self.instr} {self.in2} -> {self.out}'

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
z_wires = sorted([k for k in gate_dict if k.startswith('z')])

def find_gate(instr, in1, in2):
    for gate in gates:
        if gate is None:
            continue
        if instr is not None and gate.instr != instr:
            continue
        if in1 is not None and gate.in1 != in1 and gate.in2 != in1:
            continue
        if in2 is not None and gate.in2 != in2 and gate.in1 != in2:
            continue
        return gate
    return None

def valid_gates(temp_sum: Gate, sum: Gate, temp_carry: Gate, mid: Gate, carry: Gate):
    if temp_sum is None or sum is None or temp_carry is None or mid is None or carry is None:
        return False
    prev_carry = mid.get_other_input(temp_sum.out)
    if sum.instr != 'XOR' or not sum.has_inputs(prev_carry, temp_sum.out):
        return False
    return True

class Adder:
    def __init__(self, sum):
        self.sum = sum
        self.x = None
        self.y = None
        self.carry = None
    
    def __str__(self):
        s = ''
        s += f'x: {self.x}\n'
        s += f'y: {self.y}\n'
        s += f'sum: {self.sum}\n'
        s += f'carry: {self.carry}\n'
        return s

adders = []
for sum in z_wires:
    index = sum[1:]
    # x = 'x' + index
    # y = 'y' + index
    adder = Adder(sum)
    try:
        if sum == z_wires[0]:
            sum_gate = gate_dict[sum]
            adder.x = sum_gate.in1
            adder.y = sum_gate.in2
            carry_gate = find_gate('AND', 'x00', 'y00')
            adder.carry = carry_gate.out
        elif sum != z_wires[-1]:
            sum_gate = None
            temp_sum_gate = None
            mid_gate = None
            temp_carry_gate = None
            carry_gate = None

            x = 'x' + index
            y = 'y' + index
            prev_carry = adders[-1].carry

            sum_gate = gate_dict[sum]
            # temp_sum_gate = gate_dict[sum_gate.get_other_input(prev_carry)]
            temp_sum_gate = find_gate('XOR', x, y)
            mid_gate = find_gate('AND', temp_sum_gate.out, prev_carry)
            # temp_carry_gate = find_gate('AND', temp_sum_gate.in1, temp_sum_gate.in2)
            temp_carry_gate = find_gate('AND', x, y)
            carry_gate = find_gate('OR', mid_gate.out, temp_carry_gate.out)

            if not valid_gates(temp_sum_gate, sum_gate, temp_carry_gate, mid_gate, carry_gate):
                raise Exception('invalid adder gates')
            
            sorted_inputs = sorted([temp_sum_gate.in1, temp_sum_gate.in2])
            adder.x = sorted_inputs[0]
            adder.y = sorted_inputs[1]
            adder.carry = carry_gate.out
    except Exception:
        print('ERROR:')
        print('temp_sum_gate', temp_sum_gate)
        print('temp_carry_gate', temp_carry_gate)
        print('mid_gate', mid_gate)
        print('sum_gate', sum_gate)
        print('carry_gate', carry_gate)
        print(adder)
    else:
        print(adder)
    adders.append(adder)

# for adder in adders:
#     print(adder)