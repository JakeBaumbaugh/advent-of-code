num_keypad = [['7','8','9'], ['4','5','6'], ['1','2','3'], ['','0','A']]
dir_keypad = [['','^','A'], ['<', 'v', '>']]

sample = ['029A', '980A', '179A', '456A', '379A']
input = ['286A', '974A', '189A', '802A', '805A']

find_cache = {}
def find_key(keypad, key):
    cache_key = ('dir' if keypad == dir_keypad else 'num', key)
    if cache_key in find_cache:
        return find_cache[cache_key]
    for y in range(len(keypad)):
        for x in range(len(keypad[y])):
            if keypad[y][x] == key:
                find_cache[cache_key] = (x, y)
                return (x, y)
    find_cache[cache_key] = None
    return None

move_cache = {}
def move_instructions(keypad, start, end):
    cache_key = ('dir' if keypad == dir_keypad else 'num', start, end)
    if cache_key in move_cache:
        return move_cache[cache_key]
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
        final = lr_moves + ud_moves + 'A'
    else:
        final = ud_moves + lr_moves + 'A' if ud_first_valid else lr_moves + ud_moves + 'A'
    move_cache[cache_key] = final
    return final

valid_cache = {}
def valid_moves(keypad, point, moves):
    cache_key = ('dir' if keypad == dir_keypad else 'num', point, moves)
    if cache_key in valid_cache:
        return valid_cache
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
            valid_cache[cache_key] = False
            return False
    valid_cache[cache_key] = True
    return True

def arr_to_counts(arr):
    counts = {}
    for e in arr:
        if e in counts:
            counts[e] += 1
        else:
            counts[e] = 1
    return counts
def add_counts(c1: dict, c2: dict):
    counts = c1.copy()
    for k in c2:
        if k in counts:
            counts[k] += c2[k]
        else:
            counts[k] = c2[k]
    return counts
def mult_counts(c: dict, n: int):
    return {k : n*c[k] for k in c}

calc_cache = {}
def calc_moves(keypad, string):
    cache_key = ('dir' if keypad == dir_keypad else 'num', string)
    if cache_key in calc_cache:
        return calc_cache[cache_key]
    rob = find_key(keypad, 'A')
    moves = []
    for char in string:
        point = find_key(keypad, char)
        moves.append(move_instructions(keypad, rob, point))
        rob = point
    move_counts = arr_to_counts(moves)
    calc_cache[cache_key] = move_counts
    return move_counts


robots = 26
c = 0
for code in input:
    print('robot', robots)
    move_counts = calc_moves(num_keypad, code)
    for i in range(robots - 1):
        print('robot', robots - i - 1)
        new_counts = {}
        for move in move_counts:
            temp_counts = calc_moves(dir_keypad, move)
            temp_counts = mult_counts(temp_counts, move_counts[move])
            new_counts = add_counts(new_counts, temp_counts)
        move_counts = new_counts
    c += sum([len(k) * move_counts[k] for k in move_counts]) * int(code[:-1])

# c = sum([complexity(code) for code in input])
print(c)
