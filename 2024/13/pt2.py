import re

def add_point(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])
def sub_point(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1])
def mult_point(p1, c):
    return (p1[0] * c, p1[1] * c)

class Machine:
    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        self.prize = prize
    
    def tokens_to_win(self):
        numerator = self.prize[0] * self.a[1] - self.prize[1] * self.a[0]
        denominator = self.b[0] * self.a[1] - self.b[1] * self.a[0]
        b = numerator / denominator
        a = (self.prize[0] - self.b[0] * b) / self.a[0]
        if a.is_integer() and b.is_integer():
            return 3 * int(a) + int(b)
        return -1

with open('input.txt', 'r') as file:
    lines = file.readlines()

machines = []
while len(lines) > 0:
    match = re.search('Button A: X\\+(\\d+), Y\\+(\\d+)', lines[0])
    a = (int(match.group(1)), int(match.group(2)))
    match = re.search('Button B: X\\+(\\d+), Y\\+(\\d+)', lines[1])
    b = (int(match.group(1)), int(match.group(2)))
    match = re.search('Prize: X=(\\d+), Y=(\\d+)', lines[2])
    prize = (10000000000000 + int(match.group(1)), 10000000000000 + int(match.group(2)))
    machines.append(Machine(a, b, prize))
    lines = lines[4:]

tokens = 0
for machine in machines:
    print(machine, tokens)
    tokens_to_win = machine.tokens_to_win()
    if tokens_to_win > 0:
        tokens += tokens_to_win
print(tokens)