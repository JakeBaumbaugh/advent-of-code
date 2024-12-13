with open('input.txt', 'r') as file:
    lines = file.readlines()

transforms = {}
for line in lines[:-2]:
    k, v = line[:-1].split(' => ')
    if k in transforms:
        transforms[k].append(v)
    else:
        transforms[k] = [v]

molecule = lines[-1][:-1]
molecules = set()
for i in range(len(molecule)):
    before_molecule = molecule[:i]
    transform_molecule = molecule[i:]
    for key in transforms:
        if transform_molecule.startswith(key):
            for value in transforms[key]:
                molecules.add(before_molecule + value + transform_molecule[len(key):])

print(len(molecules))