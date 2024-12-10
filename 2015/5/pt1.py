with open('input.txt', 'r') as file:
    lines = file.readlines()

def is_nice(line: str):
    if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
        return False
    vowels = line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u')
    if vowels < 3:
        return False
    for i in range(len(line) - 1):
        if line[i] == line[i+1]:
            return True
    return False

count = 0
for line in lines:
    if is_nice(line[:-1]):
        count += 1
print(count)