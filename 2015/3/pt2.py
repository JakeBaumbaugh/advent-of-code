with open('input.txt', 'r') as file:
    line = file.readline()[:-1]

houses = set()
start_coord = [(0, 0), (0, 0)]
coord_turn = 0
houses.add(start_coord[0])
for char in line:
    curr_coord = start_coord[coord_turn]
    if char == '^':
        curr_coord = (curr_coord[0], curr_coord[1] - 1)
    elif char == 'v':
        curr_coord = (curr_coord[0], curr_coord[1] + 1)
    elif char == '<':
        curr_coord = (curr_coord[0] - 1, curr_coord[1])
    elif char == '>':
        curr_coord = (curr_coord[0] + 1, curr_coord[1])
    houses.add(curr_coord)
    start_coord[coord_turn] = curr_coord
    coord_turn = (coord_turn + 1) % 2
print(len(houses))