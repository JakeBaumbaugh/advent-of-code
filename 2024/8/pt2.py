with open('input.txt', 'r') as file:
    lines = file.readlines()
map = [list(line[:-1]) for line in lines]
antenna_map = {}
def add_antenna(char, pos):
    if char in antenna_map:
        antenna_map[char].append(pos)
    else:
        antenna_map[char] = [pos]
def pos_in_map(pos):
    return pos[1] >= 0 \
        and pos[1] < len(map) \
        and pos[0] >= 0 \
        and pos[0] < len(map[pos[1]])
def get_antinodes(pos, step):
    antinodes = set()
    antinodes.add(pos)
    step_count = 1
    while True:
        plus_pos = (pos[0] + step_count*step[0], pos[1] + step_count*step[1])
        minus_pos = (pos[0] - step_count*step[0], pos[1] - step_count*step[1])
        if pos_in_map(plus_pos) or pos_in_map(minus_pos):
            if pos_in_map(plus_pos):
                antinodes.add(plus_pos)
            if pos_in_map(minus_pos):
                antinodes.add(minus_pos)
        else:
            break
        step_count += 1
    return antinodes


for y in range(len(map)):
    for x in range(len(map[0])):
        char = map[y][x]
        if char != '.':
            add_antenna(char, (x, y))

antinodes = set()
c = []
for char in antenna_map.keys():
    antennas: list = antenna_map[char]
    for i in range(0, len(antennas)):
        cp_antennas = antennas.copy()
        start_antenna = cp_antennas.pop(i)
        for end_antenna in cp_antennas:
            step = (end_antenna[0] - start_antenna[0], end_antenna[1] - start_antenna[1])
            antinodes = antinodes.union(get_antinodes(start_antenna, step))

print(antinodes)
print(len(antinodes))
