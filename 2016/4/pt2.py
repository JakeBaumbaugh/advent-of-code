import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'

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

def decrypt(name, shift):
    decrpyted = ''
    for char in name:
        if char == '-':
            decrpyted += ' '
            continue
        index = alphabet.index(char)
        new_index = (index + shift) % len(alphabet)
        decrpyted += alphabet[new_index]
    return decrpyted

decrypted = []
for line in lines:
    match = re.search('([a-z\-]+)-(\d+)\[([a-z]+)\]', line)
    if match is None:
        continue
    name = match.group(1)
    if match.group(3) == calc_checksum(name):
        id = int(match.group(2))
        decrypted.append((decrypt(name, id), id))

for d in decrypted:
    if 'stor' in d[0]:
        print(d)