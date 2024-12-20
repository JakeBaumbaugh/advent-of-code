buttons = [[' ', ' ', '1', ' ',' '],
           [' ', '2', '3', '4',' '],
           ['5', '6', '7', '8','9'],
           [' ', 'A', 'B', 'C',' '],
           [' ', ' ', 'D', ' ',' ']]

x = 0
y = 2
def up():
    global y
    new_y = min(4, max(0, y-1))
    if buttons[new_y][x] != ' ':
        y = new_y
def down():
    global y
    new_y = min(4, max(0, y+1))
    if buttons[new_y][x] != ' ':
        y = new_y
def left():
    global x
    new_x = min(4, max(0, x-1))
    if buttons[y][new_x] != ' ':
        x = new_x
def right():
    global x
    new_x = min(4, max(0, x+1))
    if buttons[y][new_x] != ' ':
        x = new_x

dir_map = {'U': up, 'D': down, 'L': left, 'R': right}

with open('input.txt', 'r') as file:
    lines = file.readlines()

code = ''
for line in lines:
    for char in line[:-1]:
        dir_map[char]()
    code += buttons[y][x]
print(code)