# returns (count, char)
def cut_first_chars(line: str):
    return (len(line) - len(line.lstrip(line[0])), line[0])

line = '1321131112'
print(0, len(line))
for i in range(50):
    new_line = ''
    while len(line) > 0:
        count, char = cut_first_chars(line)
        new_line += str(count) + str(char)
        line = line[count:]
    line = new_line
    print(i+1, len(line))

print(len(line))