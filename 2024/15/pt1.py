with open('input.txt', 'r') as file:
    lines = file.readlines()

map_lines = []
moves = ''
is_map = True
for line in lines: 
    if len(line.strip()) == 0:
        # parse moves and break
        is_map = False
        continue
    if is_map:
        map_lines.append(line[:-1])
    else:
        moves += line.strip()

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

def move_box(pos, dir):
    if pos not in boxes:
        raise pos + 'not a box'
    next_pos = add_pos(pos, dir)
    if next_pos in walls:
        return False
    if next_pos in boxes:
        can_move = move_box(next_pos, dir)
        if can_move:
            boxes.remove(pos)
            boxes.add(next_pos)
            return True
        else:
            return False
    if next_pos == robot:
        return False
    boxes.remove(pos)
    boxes.add(next_pos)
    return True

def move_dir(dir):
    global robot
    next_pos = add_pos(robot, dir)
    if next_pos in walls:
        return False
    if next_pos in boxes:
        if move_box(next_pos, dir):
            robot = next_pos
            return True
        else:
            return False
    robot = next_pos
    return True

for char in moves:
    dir = dirs[char]
    move_dir(dir)

score = 0
for box in boxes:
    score += 100 * box[1] + box[0]
print('score', score)