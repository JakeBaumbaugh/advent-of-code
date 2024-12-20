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

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def get_path(walls, start, end):
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
    return point_dict

time_dict = {}
def get_time(walls, start, end):
    key = (start, end)
    if key in time_dict:
        return time_dict[key]
    path = get_path(walls, start, end)
    time_dict[key] = path[end]
    return path[end]

time_saves = {}
def add_time_save(k):
    if k in time_saves:
        time_saves[k] += 1
    else:
        time_saves[k] = 1
point_dict = get_path(walls, start, end)
best_count = 0
for p1 in point_dict:
    for p2 in point_dict:
        if p1 == p2 or point_dict[p1] >= point_dict[p2]:
            # same point or wrong order
            continue
        distance = dist(p1, p2)
        if distance > 20:
            # too far
            continue
        if point_dict[p2] - point_dict[p1] - distance < 100:
            # not good enough
            continue
        skip_time = point_dict[p1] + distance + get_time(walls, p2, end)
        time_saved = point_dict[end] - skip_time
        if time_saved >= 100:
            add_time_save(time_saved)
            best_count += 1

print(time_saves)
print(best_count)