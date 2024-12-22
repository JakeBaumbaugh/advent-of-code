with open('input.txt', 'r') as file:
    lines = file.readlines()

def abba(string: str):
    for i in range(len(string) - 3):
        if string[i] == ' ' or string[i+1] == ' ':
            continue
        if string[i] != string[i+1] and string[i] == string[i+3] and string[i+1] == string[i+2]:
            return True
    return False
    
count = 0
for line in lines:
    line = line.strip()
    print('line', line)
    while '[' in line:
        left_ind = line.find('[')
        right_ind = line.find(']') + 1
        inner = line[(left_ind + 1):(right_ind - 1)]
        if abba(inner):
            print('break', line)
            break
        line = line[:left_ind] + ' ' +  line[right_ind:]
    else:
        print('else', line)
        if abba(line):
            print('count', line)
            count += 1
print(count)
    