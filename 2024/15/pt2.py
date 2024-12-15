import os

with open('input.txt', 'r') as file:
    lines = file.readlines()

map_lines = []
moves = ''
is_map = True
for line in lines: 
    line = line.strip()
    if len(line) == 0:
        # parse moves and break
        is_map = False
        continue
    if is_map:
        line = line.replace('#', '##')
        line = line.replace('.', '..')
        line = line.replace('O', 'O.')
        line = line.replace('@', '@.')
        map_lines.append(line)
    else:
        moves += line

width = len(map_lines[0])
height = len(map_lines)

walls = set()
boxes = set()
robot = (0, 0)

dirs = {
    '<': (-1 ,0),
    '^': (0, -1),
    'v': (0, 1),
    '>': (1, 0)
}
def add_pos(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])
def left(pos):
    return add_pos(pos, dirs['<'])
def right(pos):
    return add_pos(pos, dirs['>'])

def print_map():
    drawing = ''
    for y in range(height):
        row = ''
        for x in range(width):
            pos = (x, y)
            if pos == robot:
                row += '\033[92m@\033[0m'
            elif pos in walls:
                row += '#'
            elif pos in boxes:
                row += '['
            elif left(pos) in boxes:
                row += ']'
            else:
                row += '.'
        drawing += row + '\n'
    print(drawing)

for y in range(len(map_lines)):
    for x in range(len(map_lines[y])):
        char = map_lines[y][x]
        if char == '@':
            robot = (x, y)
        elif char == '#':
            walls.add((x, y))
        elif char == 'O':
            boxes.add((x, y))

print('parsed objects')

def move_box(pos, dir, boxes):
    if pos not in boxes:
        raise str(pos) + 'not a box'
    new_boxes = boxes.copy()
    new_boxes.remove(pos)
    next_pos = add_pos(pos, dir)
    next_pos_2 = right(next_pos)
    if next_pos in walls or next_pos_2 in walls or next_pos == robot or next_pos_2 == robot:
        print('box', pos, 'hit wall', next_pos, 'or', next_pos_2, 'moving', dir)
        return False, boxes
    if next_pos in new_boxes or left(next_pos) in new_boxes:
        other_box_pos = next_pos if next_pos in new_boxes else left(next_pos)
        moved, new_new_boxes = move_box(other_box_pos, dir, new_boxes)
        if moved:
            new_boxes = new_new_boxes
            print('box', pos, 'pushed box', other_box_pos, 'moving', dir)
        else:
            return False, boxes
    if next_pos_2 in new_boxes:
        moved, new_new_boxes = move_box(next_pos_2, dir, new_boxes)
        if moved:
            new_boxes = new_new_boxes
            print('box', pos, 'right half pushed box', next_pos_2, 'moving', dir)
        else:
            return False, boxes
    new_boxes.add(next_pos)
    return True, new_boxes

def move_dir(dir):
    global robot, boxes
    next_pos = add_pos(robot, dir)
    if next_pos in walls:
        return False
    if next_pos in boxes or left(next_pos) in boxes:
        box_pos = next_pos if next_pos in boxes else left(next_pos)
        moved, new_boxes = move_box(box_pos, dir, boxes)
        if moved:
            boxes = new_boxes
        else:
            return False
    robot = next_pos
    return True

print(len(boxes), 'boxes before')

for char in moves:
    dir = dirs[char]
    move_dir(dir)
    # os.system('clear')
    # print_map()
    # input()

score = 0
print(len(boxes), 'boxes after')
for box in boxes:
    score += 100 * box[1] + box[0]
print('score', score)