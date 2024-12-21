num_keypad = [['7','8','9'], ['4','5','6'], ['1','2','3'], ['','0','A']]
dir_keypad = [['','^','A'], ['<', 'v', '>']]

sample = ['029A', '980A', '179A', '456A', '379A']
input = ['286A', '974A', '189A', '802A', '805A']

def find_key(keypad, key):
    for y in range(len(keypad)):
        for x in range(len(keypad[y])):
            if keypad[y][x] == key:
                return (x, y)
    return None
def moves(keypad, start, end):
    start_point = start
    end_point = end
    lr_moves = ''
    ud_moves = ''
    if end_point[0] > start_point[0]:
        lr_moves += '>' * (end_point[0] - start_point[0])
    elif end_point[0] < start_point[0]:
        lr_moves += '<' * (start_point[0] - end_point[0])
    if end_point[1] > start_point[1]:
        ud_moves += 'v' * (end_point[1] - start_point[1])
    elif end_point[1] < start_point[1]:
        ud_moves += '^' * (start_point[1] - end_point[1])
    lr_first_valid = valid_moves(keypad, start_point, lr_moves + ud_moves + 'A')
    ud_first_valid = valid_moves(keypad, start_point, ud_moves + lr_moves + 'A')
    if '<' in lr_moves and lr_first_valid:
        return lr_moves + ud_moves + 'A'
    return ud_moves + lr_moves + 'A' if ud_first_valid else lr_moves + ud_moves + 'A'

def valid_moves(keypad, point, moves):
    point = (point[0], point[1])
    for move in moves:
        if move == 'v':
            point = (point[0], point[1] + 1)
        elif move == '^':
            point = (point[0], point[1] - 1)
        elif move == '<':
            point = (point[0] - 1, point[1])
        elif move == '>':
            point = (point[0] + 1, point[1])

        if keypad[point[1]][point[0]] == '':
            return False
    return True

def calc_options(keypad, string):
    rob = find_key(keypad, 'A')
    options = []
    for char in string:
        target = find_key(keypad, char)


def calc_moves(string):
    rob_1 = find_key(dir_keypad, 'A')
    rob_2 = find_key(dir_keypad, 'A')
    rob_3 = find_key(num_keypad, 'A')
    moves_3_str = ''
    moves_2_str = ''
    moves_1_str = ''
    for char_3 in string:
        point_3 = find_key(num_keypad, char_3)
        moves_3 = moves(num_keypad, rob_3, point_3)
        rob_3 = point_3
        moves_3_str += moves_3
        for char_2 in moves_3:
            point_2 = find_key(dir_keypad, char_2)
            moves_2 = moves(dir_keypad, rob_2, point_2)
            rob_2 = point_2
            moves_2_str += moves_2
            for char_1 in moves_2:
                point_1 = find_key(dir_keypad, char_1)
                moves_1 = moves(dir_keypad, rob_1, point_1)
                rob_1 = point_1
                moves_1_str += moves_1
    return moves_3_str, moves_2_str, moves_1_str

def complexity(code):
    print(code)
    move_strs = calc_moves(code)
    for move_str in move_strs:
        print(move_str)
    buttons = move_strs[-1]
    print(len(buttons))
    print()
    return len(buttons) * int(code[:-1])

c = sum([complexity(code) for code in input])
print(c)
