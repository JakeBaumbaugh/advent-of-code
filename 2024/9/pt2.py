with open('input.txt', 'r') as file:
    line = file.readline()
line = [int(c) for c in line if c != '\n']

class File:
    def __init__(self, size: int, free: bool, id=0):
        self.size = size
        self.free = free
        self.id = id
    
    def get_mem(self):
        char = '.' if self.free else self.id
        return [char for _ in range(self.size)]

    def __str__(self):
        return f"(size={self.size}, free={self.free}, id={self.id})"

mem = []

# parse mem
file_id = 0
file_free_space = True # file T, free space F
for char in line:
    if file_free_space:
        mem.append(File(char, False, file_id))
        file_id += 1
    else:
        mem.append(File(char, True))
    file_free_space = not file_free_space

print([str(f) for f in mem[:10]])

def find_free_index(file):
    for i in range(len(mem)):
        if mem[i] is file:
            break
        if mem[i].free and mem[i].size >= file.size:
            return i
    return -1

# compact mem
i = len(mem) - 1
while i >= 0:
    file = mem[i]
    if file.free:
        i -= 1
        continue
    free_index = find_free_index(file)
    if free_index == -1:
        i -= 1
        continue
    mem[free_index].size -= file.size
    mem[i] = File(file.size, True)
    if mem[free_index].size > 0:
        mem.insert(free_index, file)
    else:
        mem[free_index] = file
    i -= 1

print([str(f) for f in mem[:10]])

# full_mem
full_mem = []
for file in mem:
    full_mem.extend(file.get_mem())

print(full_mem[:30])

# checksum
sum = 0
for i in range(len(full_mem)):
    if full_mem[i] != '.':
        sum += i * full_mem[i]

print(sum)