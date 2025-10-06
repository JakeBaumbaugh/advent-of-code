import re

with open('input.txt', 'r') as file:
    text = file.readline()[:-1]

output = ''
index = 0
while index < len(text):
    subtext = text[index:]
    match = re.match('\\((\\d+)x(\\d+)\\)', subtext)
    if match is None:
        output += subtext[0]
        index += 1
        continue
    size = int(match.group(1))
    repeats = int(match.group(2))
    skip = len(match.group(0))
    section = subtext[skip:skip+size]
    output += section * repeats
    index += skip + size

print(len(output))