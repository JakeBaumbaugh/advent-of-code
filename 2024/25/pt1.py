with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

keys = []
locks = []
def read_block(block):
    is_key = block[0] == '.....'
    pin_counts = []
    for i in range(5):
        col = [block[j][i] for j in range(7)]
        pins = len([c for c in col if c == '#']) - 1
        pin_counts.append(pins)
    if is_key:
        keys.append(pin_counts)
    else:
        locks.append(pin_counts)

i = 0
while i < len(lines):
    start = i
    end = i + 7
    read_block(lines[start:end])
    i += 8

def match(key, lock):
    for i in range(5):
        if key[i] + lock[i] > 5:
            return False
    return True

count = 0
for key in keys:
    for lock in locks:
        if match(key, lock):
            count += 1
print(count)