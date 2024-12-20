with open('input.txt', 'r') as file:
    lines = file.readlines()

char_counts = []
for _ in lines[0].strip():
    char_counts.append({})

for line in lines:
    line = line.strip()
    for i in range(len(line)):
        char_count = char_counts[i]
        char = line[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

most_message = ''
least_message = ''
for char_count in char_counts:
    keys = sorted(char_count.keys(), key=lambda k : char_count[k])
    most_message += keys[-1]
    least_message += keys[0]
print('part 1:', most_message)
print('part 2:', least_message)