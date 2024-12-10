with open('input.txt', 'r') as file:
    lines = file.readlines()

sum = 0
for line in lines:
    line = line[:-1]
    sum += 2 + line.count('\"') + line.count('\\')
print(sum)