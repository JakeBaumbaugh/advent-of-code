def gen_coords(i, j):
    return [
        [(i,j), (i+1, j), (i+2, j), (i+3, j)],
        [(i,j), (i-1, j), (i-2, j), (i-3, j)],
        [(i,j), (i, j+1), (i, j+2), (i, j+3)],
        [(i,j), (i, j-1), (i, j-2), (i, j-3)],
        [(i,j), (i+1, j+1), (i+2, j+2), (i+3, j+3)],
        [(i,j), (i+1, j-1), (i+2, j-2), (i+3, j-3)],
        [(i,j), (i-1, j+1), (i-2, j+2), (i-3, j+3)],
        [(i,j), (i-1, j-1), (i-2, j-2), (i-3, j-3)]
    ]

def valid_coord(max_i, max_j, coord):
    return coord[0] >= 0 and coord[0] < max_i and coord[1] >= 0 and coord[1] < max_j

def valid_coords(max_i, max_j, coords):
    for coord in coords:
        if not valid_coord(max_i, max_j, coord):
            return False
    return True

with open('input.txt', 'r') as file:
    lines = file.readlines()
grid = [[c for c in line if c != '\n'] for line in lines]

def check_coords(coords):
    return grid[coords[0][0]][coords[0][1]] == 'X' \
        and grid[coords[1][0]][coords[1][1]] == 'M' \
        and grid[coords[2][0]][coords[2][1]] == 'A' \
        and grid[coords[3][0]][coords[3][1]] == 'S' \

count = 0
for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        coords_set = gen_coords(i, j)
        for coords in coords_set:
            if not valid_coords(len(grid), len(grid[i]), coords):
                continue
            if check_coords(coords):
                count += 1

print(count)
        