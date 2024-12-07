with open('input.txt', 'r') as file:
    lines = file.readlines()
map = [list(line[:-1]) for line in lines]

guard_line = [line for line in map if '^' in line][0]
guard_y = map.index(guard_line)
guard_x = guard_line.index('^')
guard_pos = (guard_x, guard_y)

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir_index = 0

def inc_dir():
    global dir_index
    dir_index = (dir_index + 1) % 4
def get_dir():
    return dirs[dir_index]
def get_char(pos):
    return map[pos[1]][pos[0]]
def get_next_pos():
    dir = get_dir()
    return (guard_pos[0] + dir[0], guard_pos[1] + dir[1])
def pos_in_map():
    return guard_pos[0] >= 0 \
        and guard_pos[0] < len(guard_line) \
        and guard_pos[1] >= 0 \
        and guard_pos[1] < len(map)
positions = {guard_pos}

while pos_in_map():
    next_pos = get_next_pos()
    try:
        while get_char(next_pos) == '#':
            inc_dir()
            next_pos = get_next_pos()
    except:
        break
    positions.add(next_pos)
    guard_pos = next_pos
    print("going to ", guard_pos)
    

print(len(positions))