def parse_line(line):
    parts = line.split(',')
    return (int(parts[0]), int(parts[1]))

with open('input.txt', 'r') as file:
    lines = file.readlines()

def get_adj(point, walls):
    points = []
    if point[0] + 1 <= 70 and (point[0] + 1, point[1]) not in walls:
        points.append((point[0] + 1, point[1]))
    if point[0] - 1 >= 0 and(point[0] - 1, point[1]) not in walls:
        points.append((point[0] - 1, point[1]))
    if point[1] + 1 <= 70 and (point[0], point[1] + 1) not in walls:
        points.append((point[0], point[1] + 1))
    if point[1] - 1 >= 0 and (point[0], point[1] - 1) not in walls:
        points.append((point[0], point[1] - 1))
    return points
    

width = 70
height = 70

def get_steps_to_end(walls):
    step = 0
    point_dict = {(0,0): 0}
    visited = {(0,0)}
    while (70, 70) not in point_dict:
        if len(visited) == 0:
            return -1
        step += 1
        new_visited = set()
        for point in visited:
            adj_points = get_adj(point, walls)
            for adj_point in adj_points:
                if adj_point not in point_dict or point_dict[adj_point] > step:
                    point_dict[adj_point] = step
                    new_visited.add(adj_point)
        visited = new_visited
    return point_dict[(70, 70)]



cutoff = len(lines) // 2
cutoff_diff = cutoff // 2

walls = [parse_line(line) for line in lines]
while True:
    steps = get_steps_to_end(walls[:cutoff])
    if steps == -1:
        prev_steps = get_steps_to_end(walls[:(cutoff - 1)])
        if prev_steps == -1:
            cutoff -= cutoff_diff
        else:
            print(walls[cutoff - 1])
            break
    else:
        cutoff += cutoff_diff
    cutoff_diff = max(1, cutoff_diff // 2)