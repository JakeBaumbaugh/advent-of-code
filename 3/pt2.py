import re

with open('input.txt', 'r') as file:
    txt = file.read()

matches = re.findall("(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))", txt)
print(matches)
sum = 0
enabled = True
for match in matches:
    if match[2].startswith("don't"):
        enabled = False
    elif match[1].startswith("do"):
        enabled = True
    elif enabled:
        s = match[0].split('(')[1]
        s = s.split(')')[0]
        [a, b] = s.split(',')
        sum += int(a) * int(b)
print(sum)
