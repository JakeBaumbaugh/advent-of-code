with open('input.txt', 'r') as file:
    line = file.readline()[:-1]

houses = set()
start_coord = (0, 0)
houses.add(start_coord)
for char in line:
    if char == '^':
        start_coord = (start_coord[0], start_coord[1] - 1)
    elif char == 'v':
        start_coord = (start_coord[0], start_coord[1] + 1)
    elif char == '<':
        start_coord = (start_coord[0] - 1, start_coord[1])
    elif char == '>':
        start_coord = (start_coord[0] + 1, start_coord[1])
    houses.add(start_coord)
print(len(houses))