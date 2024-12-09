with open('input.txt', 'r') as file:
    line = file.readline()
line = [int(c) for c in line if c != '\n']
mem = []
file_free_space = True # file T, free space F
file_id = 0

# parse mem
for char in line:
    if file_free_space:
        mem.extend([file_id for _ in range(char)])
        file_id += 1
    else:
        mem.extend(['.' for _ in range(char)])
    file_free_space = not file_free_space

print(mem[:30])

def pop_block():
    char = mem.pop()
    while char == '.':
        char = mem.pop()
    return char

# compact mem
i = 0
while i < len(mem):
    if mem[i] == '.':
        block = pop_block()
        if i >= len(mem):
            mem.append(block)
            break
        mem[i] = block
    i += 1


print(mem[:30])

# checksum
sum = 0
for i in range(len(mem)):
    sum += i * mem[i]
print(sum)