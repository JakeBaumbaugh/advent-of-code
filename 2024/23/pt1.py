with open('input.txt', 'r') as file:
    lines = file.readlines()

connections = {}
def add_connection(c1, c2):
    if c1 not in connections:
        connections[c1] = set()
    if c2 not in connections:
        connections[c2] = set()
    connections[c1].add(c2)
    connections[c2].add(c1)
def name_3(c1, c2, c3):
    return '-'.join(sorted([c1, c2, c3]))

for line in lines:
    c1, c2 = line.strip().split('-')
    add_connection(c1, c2)

threeways = set()
for c1 in connections:
    for c2 in connections[c1]:
        for c3 in connections[c1]:
            if c1 == c2 or c1 == c3 or c2 == c3:
                continue
            if c3 in connections[c2]:
                threeways.add(name_3(c1, c2, c3))

t_threeways = [threeway for threeway in threeways if threeway[0] == 't' or threeway[3] == 't' or threeway[6] == 't']
print(len(t_threeways))