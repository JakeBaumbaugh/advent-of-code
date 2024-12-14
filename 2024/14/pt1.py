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

for i in range(100):
    for robot in robots:
        robot.move()

quadrant_counts = [0, 0, 0, 0]
for robot in robots:
    x, y = robot.pos
    if x < mid_x and y < mid_y:
        quadrant_counts[0] += 1
    elif x < mid_x and y > mid_y:
        quadrant_counts[1] += 1
    elif x > mid_x and y < mid_y:
        quadrant_counts[2] += 1
    elif x > mid_x and y > mid_y:
        quadrant_counts[3] += 1

print(quadrant_counts[0] * quadrant_counts[1] * quadrant_counts[2] * quadrant_counts[3])