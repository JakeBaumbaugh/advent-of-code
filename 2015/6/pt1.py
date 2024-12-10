import re

with open('input.txt', 'r') as file:
    lines = file.readlines()

lights = [[False for x in range(1000)] for y in range(1000)]

def turn_on(start_coord, end_coord):
    # print("turning on", start_coord, "through", end_coord)
    for i in range(start_coord[0], end_coord[0] + 1):
        for j in range(start_coord[1], end_coord[1] + 1):
            lights[j][i] = True

def turn_off(start_coord, end_coord):
    # print("turning off", start_coord, "through", end_coord)
    for i in range(start_coord[0], end_coord[0] + 1):
        for j in range(start_coord[1], end_coord[1] + 1):
            lights[j][i] = False

def toggle(start_coord, end_coord):
    # print("toggling", start_coord, "through", end_coord)
    for i in range(start_coord[0], end_coord[0] + 1):
        for j in range(start_coord[1], end_coord[1] + 1):
            lights[j][i] = not lights[j][i]

for line in lines:
    match = re.search('(.+) (\d+),(\d+) through (\d+),(\d+)', line[:-1])
    instruction = match.group(1)
    start_coord = (int(match.group(2)), int(match.group(3)))
    end_coord = (int(match.group(4)), int(match.group(5)))
    if instruction == 'turn on':
        turn_on(start_coord, end_coord)
    elif instruction == 'turn off':
        turn_off(start_coord, end_coord)
    elif instruction == 'toggle':
        toggle(start_coord, end_coord)

lights_on = 0
for i in range(1000):
    for j in range(1000):
        if lights[j][i]:
            lights_on += 1
print(lights_on)