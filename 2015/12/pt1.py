import re

with open('input.txt', 'r') as file:
    json = file.readline()[:-1]

matches = re.findall('(-?\\d+)', json)
sum = 0
for match in matches:
    sum += int(match)
print(sum)