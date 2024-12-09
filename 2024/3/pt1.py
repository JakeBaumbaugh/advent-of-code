import re

with open('input.txt', 'r') as file:
    txt = file.read()

matches = re.findall("mul\(\d{1,3},\d{1,3}\)", txt)
sum = 0
for match in matches:
    s = match.split('(')[1]
    s = s.split(')')[0]
    [a, b] = s.split(',')
    sum += int(a) * int(b)
print(sum)
