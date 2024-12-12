with open('input.txt', 'r') as file:
    lines = file.readlines()
map = [list(line[:-1]) for line in lines]
for y in range(len(map)):
    for x in range(len(map[y])):
        map[y][x] = map[y][x] == '#'

def get_light(point):
    return point_in_map(point) and map[point[1]][point[0]]
def point_in_map(point):
    return point[1] >= 0 and point[1] < len(map) and point[0] >= 0 and point[0] < len(map[y])
def count_neighbors(point):
    dirs = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
    neighbors = [(point[0] + dir[0], point[1] + dir[1]) for dir in dirs]
    return sum([1 if get_light(point) else 0 for point in neighbors])
def next_state(point):
    if get_light(point):
        return 2 <= count_neighbors(point) <= 3
    else:
        return count_neighbors(point) == 3

for i in range(100):
    new_map = [row.copy() for row in map]
    for y in range(len(map)):
        for x in range(len(map[y])):
            new_map[y][x] = next_state((x,y))
    map = new_map
    print(i+1)

on_lights = 0
for row in map:
    on_lights += sum([1 if light else 0 for light in row])
print(on_lights)