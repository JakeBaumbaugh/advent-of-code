with open('input.txt', 'r') as file:
    lines = file.readlines()
map = [list(line[:-1]) for line in lines]

trails = []

for j in range(len(map)):
    for i in range(len(map[j])):
        if map[j][i] == '0':
            trails.append([(i, j)])

def get_char(x, y):
    if y >= 0 and y < len(map) and x >= 0 and x < len(map[y]):
        return map[y][x]
    else:
        return -1

def find_num_trail(num):
    global trails
    new_trails = []
    for trail in trails:
        last_x, last_y = trail[-1]
        if get_char(last_x, last_y-1) == num:
            new_trails.append([*trail, (last_x, last_y-1)])
        if get_char(last_x, last_y+1) == num:
            new_trails.append([*trail, (last_x, last_y+1)])
        if get_char(last_x-1, last_y) == num:
            new_trails.append([*trail, (last_x-1, last_y)])
        if get_char(last_x+1, last_y) == num:
            new_trails.append([*trail, (last_x+1, last_y)])
    trails = new_trails

for i in range(1, 10):
    find_num_trail(str(i))

unique_trails = {}
for trail in trails:
    unique_trails[(trail[0], trail[-1])] = trail
print("part 1:", len(unique_trails))
print("part 2:", len(trails))