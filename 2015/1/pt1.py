with open('input.txt', 'r') as file:
    line = file.readline()[:-1]

floor = 0
for char in line:
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1

print(floor)