import sys

with open('input.txt', 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

sys.setrecursionlimit(len(lines)**2)

walls = set()
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '#':
            walls.add((x, y))
        if lines[y][x] == 'S':
            start = (x, y)
        if lines[y][x] == 'E':
            end = (x, y)

dir_map = {
    'S': (0, 1),
    'N': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}
next_dir_map = {
    'S': ['S', 'E', 'W'],
    'N': ['N', 'E', 'W'],
    'E': ['E', 'N', 'S'],
    'W': ['W', 'N', 'S']
}


def add_point(a, b):
    return (a[0] + b[0], a[1] + b[1])
def best_path(a, b, dir, visited={}, curr_score=0):
    if a == b:
        return 0, [[a]]
    if a in visited:
        visited[a] = min(curr_score, visited[a])
    else:
        visited[a] = curr_score
    next = [(add_point(a, dir_map[dir]), dir) for dir in next_dir_map[dir]]
    next = [tup for tup in next if tup[0] not in walls and (tup[0] not in visited or visited[tup[0]] + 1000 >= curr_score)]
    best_score = 99999999999999
    best_paths = []
    for (point, next_dir) in next:
        score_add = 1 if next_dir == dir else 1001
        path_score, paths = best_path(point, b, next_dir, visited, score_add + curr_score)
        score = score_add + path_score
        if score < best_score:
            best_score = score
            best_paths = paths
        elif score == best_score:
            best_paths.extend(paths)
    return best_score, [[a, *path] for path in best_paths]

best_score, best_paths = best_path(start, end, 'E')
best_path_points = set()
for path in best_paths:
    for point in path:
        best_path_points.add(point)
print(best_score, len(best_paths), len(best_path_points))