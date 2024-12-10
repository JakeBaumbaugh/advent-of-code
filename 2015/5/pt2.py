with open('input.txt', 'r') as file:
    lines = file.readlines()

def abxab(line: str):
    for i in range(len(line) - 3):
        chars = line[i:i+2]
        if chars in line[i+2:]:
            return True
    return False

def axa(line: str):
    for i in range(len(line) - 2):
        if line[i] == line[i+2]:
            return True
    return False

def is_nice(line: str):
    return abxab(line) and axa(line)

count = 0
for line in lines:
    if is_nice(line[:-1]):
        count += 1
print(count)