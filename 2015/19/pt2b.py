import re

with open('input.txt', 'r') as file:
    lines = file.readlines()
target = lines[-1][:-1]

transforms = {}
for line in lines[:-2]:
    k, v = line[:-1].split(' => ')
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
                if new_molecule == target or len(new_molecule) < len(target):
                    molecules.add(new_molecule)
    return molecules

steps = [set()]
steps[0].add('e')
while target not in steps[-1]:
    last_step = steps[-1]
    next_step = set()
    for molecule in last_step:
        next_step = next_step.union(transform_molecule(molecule))
    print('step', len(steps), next_step)
    steps.append(next_step)
print(len(steps))