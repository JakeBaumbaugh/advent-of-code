with open('input.txt', 'r') as file:
    line = file.readline()[:-1]

floor = 0
for i in range(len(line)):
    char = line[i]
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
    if floor == -1:
        print(i + 1)
        break