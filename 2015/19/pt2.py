import re

with open('input.txt', 'r') as file:
    lines = file.readlines()
target = lines[-1][:-1]

transforms = {}
for line in lines[:-2]:
    v, k = line[:-1].split(' => ')
    if k in transforms:
        transforms[k].append(v)
    else:
        transforms[k] = [v]

def transform_molecule(molecule):
    molecules = set()
    for key in transforms:
        matches = [match for match in re.finditer(key, molecule)]
        for match in matches:
            for value in transforms[key]:
                new_molecule = molecule[:match.start()] + value + molecule[match.end():]
                if new_molecule != 'e' and 'e' in new_molecule:
                    continue
                if new_molecule == target or len(new_molecule) < len(target):
                    molecules.add(new_molecule)
    return molecules

def lev(a, b, depth=1):
    return max(len(a), len(b))
    # if depth > 10:
    #     return depth
    # print('lev', a, b)
    if len(b) == 0:
        return len(a)
    if len(a) == 0:
        return len(b)
    if a[0] == b[0]:
        return lev(a[1:], b[1:], depth)
    return 1 + min(lev(a[1:], b, depth+1), lev(a, b[1:], depth+1), lev(a[1:], b[1:], depth+1))

def recurse_molecule(molecule):
    nexts = transform_molecule(molecule)
    nexts = sorted(nexts, key=lambda x : lev(x, 'e'))
    for next in nexts:
        if next == 'e':
            return ['e']
        result = recurse_molecule(next)
        if len(result) > 0:
            return [next, *result]
    return []

result = recurse_molecule(target)
print(result)
print(len(result))
print(result[0] == target)
