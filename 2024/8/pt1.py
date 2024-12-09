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
            antinode = (2*end_antenna[0] - start_antenna[0], 2*end_antenna[1] - start_antenna[1])
            if pos_in_map(antinode):
                antinodes.add(antinode)

print(antinodes)
print(len(antinodes))
