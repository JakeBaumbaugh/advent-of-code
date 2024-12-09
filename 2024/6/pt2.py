with open('input.txt', 'r') as file:
    lines = file.readlines()
map = [list(line[:-1]) for line in lines]

guard_line = [line for line in map if '^' in line][0]
guard_y = map.index(guard_line)
guard_x = guard_line.index('^')
guard_pos = (guard_x, guard_y)

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

walls = set()
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == '#':
            walls.add((x, y))

def get_next_dir(dir):
    ind = dirs.index(dir)
    return dirs[(ind + 1) % 4]
def get_dir(dir_index):
    return dirs[dir_index]
def get_char(pos):
    return map[pos[1]][pos[0]]
def get_next_pos(pos, dir_index):
    dir = get_dir(dir_index)
    return (pos[0] + dir[0], pos[1] + dir[1])
def pos_in_map(pos):
    return pos[0] >= 0 \
        and pos[0] < len(guard_line) \
        and pos[1] >= 0 \
        and pos[1] < len(map)
def add_pos(pos_dict, pos, dir_index):
    if pos in pos_dict:
        pos_dict[pos].add(dir_index)
    else:
        pos_dict[pos] = {dir_index}

class Sim:
    def __init__(self, pos, dir_index, walls, positions={}):
        self.pos = (pos[0], pos[1])
        self.dir_index = dir_index
        self.walls = walls.copy()
        self.positions = positions.copy()
        self.print = False
    
    def is_repeat_pos(self):
        if self.print:
            print(self.pos, self.dir_index, self.positions[self.pos] if self.pos in self.positions else None)
        return self.pos in self.positions and self.dir_index in self.positions[self.pos]
    def save_pos(self):
        if self.pos in self.positions:
            self.positions[self.pos].add(self.dir_index)
        else:
            self.positions[self.pos] = {self.dir_index}
    
    def run(self):
        while pos_in_map(self.pos):
            if self.is_repeat_pos():
                return True
            next_pos = get_next_pos(self.pos, self.dir_index)
            while next_pos in self.walls:
                self.save_pos()
                self.dir_index = (self.dir_index + 1) % 4
                next_pos = get_next_pos(self.pos, self.dir_index)
            self.save_pos()
            self.pos = next_pos
        return False

main_sim = Sim(guard_pos, 0, walls)
print("main sim result:", main_sim.run())
loop_blocks = set()

count = 0
for block_pos in main_sim.positions.keys():
    block_sim_walls = walls.copy()
    block_sim_walls.add(block_pos)
    block_sim = Sim(guard_pos, 0, block_sim_walls)
    block_sim_result = block_sim.run()
    if count % 100 == 0:
        print("block sim", count, "/", len(main_sim.positions))
    if block_sim_result:
        loop_blocks.add(block_pos)
    count += 1
print(len(loop_blocks))