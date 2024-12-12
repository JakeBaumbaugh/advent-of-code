# returns (count, char)
def cut_first_chars(line: str):
    count = 0
    char = line[0]
    while line.startswith(char):
        line = line[1:]
        count += 1
    return (count, char)

line = '1321131112'
print(0, len(line))
for i in range(40):
    new_line = ''
    while len(line) > 0:
        count, char = cut_first_chars(line)
        new_line += str(count) + str(char)
        line = line[count:]
    line = new_line
    print(i+1, len(line))

print(len(line))