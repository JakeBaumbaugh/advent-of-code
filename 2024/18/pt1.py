def parse_line(line):
    parts = line.split(',')
    return (int(parts[0]), int(parts[1]))

with open('input.txt', 'r') as file:
    lines = file.readlines()

walls = [parse_line(line) for line in lines[:1024]]
def get_adj(point):
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

step = 0
point_dict = {(0,0): 0}
visited = {(0,0)}
while (70, 70) not in point_dict and len(visited) > 0:
    step += 1
    new_visited = set()
    for point in visited:
        adj_points = get_adj(point)
        for adj_point in adj_points:
            if adj_point not in point_dict or point_dict[adj_point] > step:
                point_dict[adj_point] = step
                new_visited.add(adj_point)
    visited = new_visited
    print(step, ':', visited)
print(point_dict[(70, 70)])