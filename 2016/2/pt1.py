buttons = [['1','2','3'], ['4','5','6'], ['7','8','9']]

x = 1
y = 1
def up():
    global y
    y = min(2, max(0, y-1))
def down():
    global y
    y = min(2, max(0, y+1))
def left():
    global x
    x = min(2, max(0, x-1))
def right():
    global x
    x = min(2, max(0, x+1))
dir_map = {'U': up, 'D': down, 'L': left, 'R': right}

with open('input.txt', 'r') as file:
    lines = file.readlines()

code = ''
for line in lines:
    for char in line[:-1]:
        dir_map[char]()
    code += buttons[y][x]
print(code)