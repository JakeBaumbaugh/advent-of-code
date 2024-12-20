with open('input.txt', 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

height = len(lines)
width = len(lines[0])

walls = set()
for y in range(height):
    for x in range(width):
        if lines[y][x] == '#':
            walls.add((x, y))
        elif lines[y][x] == 'S':
            start = (x, y)
        elif lines[y][x] == 'E':
            end = (x, y)

def get_adj(point, walls):
    points = []
    if point[0] + 1 <= width and (point[0] + 1, point[1]) not in walls:
        points.append((point[0] + 1, point[1]))
    if point[0] - 1 >= 0 and(point[0] - 1, point[1]) not in walls:
        points.append((point[0] - 1, point[1]))
    if point[1] + 1 <= height and (point[0], point[1] + 1) not in walls:
        points.append((point[0], point[1] + 1))
    if point[1] - 1 >= 0 and (point[0], point[1] - 1) not in walls:
        points.append((point[0], point[1] - 1))
    return points

def get_time(walls):
    step = 0
    point_dict = {start: 0}
    visited = {start}
    while end not in point_dict and len(visited) > 0:
        step += 1
        new_visited = set()
        for point in visited:
            adj_points = get_adj(point, walls)
            for adj_point in adj_points:
                if adj_point not in point_dict or point_dict[adj_point] > step:
                    point_dict[adj_point] = step
                    new_visited.add(adj_point)
        visited = new_visited
    return point_dict[end]

time = get_time(walls)

skippable_walls = set()
for wall in walls:
    if wall[0] == 0 or wall[1] == 0 or wall[0] == width - 1 or wall[1] == height - 1:
        continue
    x, y = wall
    if lines[y][x-1] != '#' and lines[y][x+1] != '#':
        skippable_walls.add(wall)
    elif lines[y-1][x] != '#' and lines[y+1][x] != '#':
        skippable_walls.add(wall)

print(len(skippable_walls), 'walls to check')
counter = 0
best_walls = set()
for wall in skippable_walls:
    new_walls = walls.copy()
    new_walls.remove(wall)
    new_time = get_time(new_walls)
    counter += 1
    if new_time + 100 <= time:
        best_walls.add(wall)
    
    print(counter, time - new_time)

print(len(best_walls))