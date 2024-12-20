with open('input.txt', 'r') as file:
    lines = file.readlines()

valid = 0
for line in lines:
    sides = line.strip().split()
    sides = sorted([int(side) for side in sides])
    if sides[0] + sides[1] > sides[2]:
        valid += 1
print(valid)