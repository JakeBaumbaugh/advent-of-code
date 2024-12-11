with open('input.txt', 'r') as file:
    lines = file.readlines()

distances = {}
def add_dist(p1, p2, dist):
    if p1 in distances:
        distances[p1][p2] = dist
    else:
        distances[p1] = {p2: dist}

    if p2 in distances:
        distances[p2][p1] = dist
    else:
        distances[p2] = {p1: dist}

def all_reorders(list):
    if len(list) <= 1:
        return [list]
    sub_reorders = all_reorders(list[:-1])
    insert = list[-1]
    reorders = []
    for sub_reorder in sub_reorders:
        for i in range(len(sub_reorder) + 1):
            reorders.append([*sub_reorder[:i], insert, *sub_reorder[i:]])
    return reorders

def calc_dist(list):
    dist = 0
    for i in range(len(list) - 1):
        p1 = list[i]
        p2 = list[i+1]
        dist += distances[p1][p2]
    return dist

for line in lines:
    line = line[:-1]
    parts = line.split(' = ')
    parts = [*parts[0].split(' to '), parts[1]]
    add_dist(parts[0], parts[1], int(parts[2]))

places = [key for key in distances]
reorders = all_reorders(places)
reorder_distances = [calc_dist(reorder) for reorder in reorders]
min_index = 0
max_index = 0
for i in range(len(reorders)):
    if reorder_distances[i] < reorder_distances[min_index]:
        min_index = i
    if reorder_distances[i] > reorder_distances[max_index]:
        max_index = i
print("part 1", reorder_distances[min_index])
print("part 2", reorder_distances[max_index])
