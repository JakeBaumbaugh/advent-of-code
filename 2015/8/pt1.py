with open('input.txt', 'r') as file:
    lines = file.readlines()

sum = 0
for line in lines:
    line = line[:-1]
    sum += 2
    while line.find('\\\\') > 0:
        index = line.index('\\\\')
        line = line[:index] + line[index+2:]
        sum += 1
    while line.find('\\"') > 0:
        index = line.index('\\"')
        line = line[:index] + line[index+2:]
        sum += 1
    while line.find('\\x') > 0:
        index = line.index('\\x')
        line = line[:index] + line[index+4:]
        sum += 3
print(sum)