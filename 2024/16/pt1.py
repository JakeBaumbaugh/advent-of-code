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
        return 0
    visited[a] = curr_score
    next = [(add_point(a, dir_map[dir]), dir) for dir in next_dir_map[dir]]
    next = [tup for tup in next if tup[0] not in walls and (tup[0] not in visited or visited[tup[0]] >= curr_score)]
    best_score = 99999999999999
    for (point, next_dir) in next:
        score_add = 1 if next_dir == dir else 1001
        best_score = min(best_score, score_add + best_path(point, b, next_dir, visited, score_add + curr_score))
    return best_score

print(best_path(start, end, 'E'))