import re

with open('input.txt', 'r') as file:
    lines = file.readlines()

sum = 0
for line in lines:
    match = re.search('(\d+)x(\d+)x(\d+)', line)
    w = int(match.group(1))
    h = int(match.group(2))
    l = int(match.group(3))
    sum += 2*w*l + 2*w*h + 2*h*l + min(w*l, w*h, h*l)
print(sum)