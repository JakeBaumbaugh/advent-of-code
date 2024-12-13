import re

def add_point(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])
def mult_point(p1, c):
    return (p1[0] * c, p1[1] * c)

class Machine:
    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        self.prize = prize
    
    def tokens_to_win(self):
        for a_count in range(101):
            for b_count in range(101):
                if add_point(mult_point(self.a, a_count), mult_point(self.b, b_count)) == self.prize:
                    print(a_count, b_count)
                    return 3 * a_count + b_count
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
    prize = (int(match.group(1)), int(match.group(2)))
    machines.append(Machine(a, b, prize))
    lines = lines[4:]

tokens = 0
for machine in machines:
    tokens_to_win = machine.tokens_to_win()
    if tokens_to_win > 0:
        tokens += tokens_to_win
print(tokens)