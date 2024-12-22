with open('input.txt', 'r') as file:
    lines = file.readlines()

screen = [[False for _ in range(50)] for _ in range(6)]

def rect(a, b):
    for y in range(b):
        for x in range(a):
            screen[y][x] = True
def rot_row(a, b):
    row = screen[a]
    new_row = [row[(i - b) % len(row)] for i in range(len(row))]
    screen[a] = new_row
def rot_column(a, b):
    col = [screen[i][a] for i in range(len(screen))]
    new_col = [col[(i - b) % len(col)] for i in range(len(col))]
    for i in range(len(new_col)):
        screen[i][a] = new_col[i]
def print_screen():
    for row in screen:
        print(''.join(['#' if val else '.' for val in row]))

for line in lines:
    line = line.strip()
    if line.startswith('rect'):
        a, b = line[5:].split('x')
        rect(int(a), int(b))
    elif line.startswith('rotate row'):
        a, b = line[13:].split(' by ')
        rot_row(int(a), int(b))
    elif line.startswith('rotate column'):
        a, b = line[16:].split(' by ')
        rot_column(int(a), int(b))

count = 0
for y in range(len(screen)):
    for x in range(len(screen[y])):
        if screen[y][x]:
            count += 1
print_screen()
print(count)