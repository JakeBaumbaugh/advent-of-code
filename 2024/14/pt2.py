import re

width = 101
height = 103
mid_x = width // 2
mid_y = height // 2

class Robot:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
    
    def move(self):
        x = (self.pos[0] + self.vel[0]) % width
        y = (self.pos[1] + self.vel[1]) % height
        self.pos = (x, y)

with open('input.txt', 'r') as file:
    lines = file.readlines()
robots = []
for line in lines:
    match = re.search('p=(-?\\d+),(-?\\d+) v=(-?\\d+),(-?\\d+)', line)
    pos = (int(match.group(1)), int(match.group(2)))
    vel = (int(match.group(3)), int(match.group(4)))
    robots.append(Robot(pos, vel))

def print_grid():
    map = [['.' for x in range(width)] for y in range(height)]
    for robot in robots:
        x, y = robot.pos
        map[y][x] = 'X'
    for line in map:
        print(''.join(line))

steps = 0
while True:
    steps += 1
    print('step', steps)
    print_grid()
    for robot in robots:
        robot.move()
    input()
print(steps)