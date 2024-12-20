with open('input.txt', 'r') as file:
    line = file.readline()[:-1]
instructions = [dir.strip() for dir in line.split(',')]

dir_list = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def dir_left(dir):
    index = dir_list.index(dir)
    return dir_list[(index - 1) % 4]
def dir_right(dir):
    index = dir_list.index(dir)
    return dir_list[(index + 1) % 4]
def add_point(a, b):
    return (a[0] + b[0], a[1] + b[1])
def mult_point(a, c):
    return (a[0] * c, a[1] * c)

dir = dir_list[0]
point = (0, 0)
for instruction in instructions:
    turn = instruction[0]
    steps = int(instruction[1:])
    if turn == 'L':
        dir = dir_left(dir)
    elif turn == 'R':
        dir = dir_right(dir)
    point = add_point(point, mult_point(dir, steps))
print(point)
print(abs(point[0]) + abs(point[1]))