import re

with open('input.txt', 'r') as file:
    lines = file.readlines()

def calc_checksum(name):
    letters = {}
    for letter in name:
        if letter == '-':
            continue
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return ''.join(sorted(letters.keys(), key=lambda k : (-1 * letters[k], k))[:5])

sum = 0
for line in lines:
    match = re.search('([a-z\-]+)-(\d+)\[([a-z]+)\]', line)
    if match is None:
        continue
    name = match.group(1)
    if match.group(3) == calc_checksum(name):
        sum += int(match.group(2))
print(sum)
