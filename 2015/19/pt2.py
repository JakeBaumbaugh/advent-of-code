import re

with open('input.txt', 'r') as file:
    lines = file.readlines()

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
                if new_molecule == 'e' or 'e' not in new_molecule:
                    molecules.add(new_molecule)
    return molecules

molecule = lines[-1][:-1]
molecule_steps = [set()]
molecule_steps[0].add(molecule)
while 'e' not in molecule_steps[-1]:
    molecules = set()
    for molecule in molecule_steps[-1]:
        transformed = transform_molecule(molecule)
        molecules = molecules.union(transformed)
    print(len(molecules))
    molecule_steps.append(molecules)

print("final", len(molecule_steps) - 1)