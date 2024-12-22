with open('input.txt', 'r') as file:
    lines = file.readlines()

def abba(string: str):
    for i in range(len(string) - 3):
        if string[i] == ' ' or string[i+1] == ' ':
            continue
        if string[i] != string[i+1] and string[i] == string[i+3] and string[i+1] == string[i+2]:
            return True
    return False
def get_aba(string: str):
    aba_set = set()
    for i in range(len(string) - 2):
        if string[i] != string[i+1] and string[i] == string[i+2]:
            aba_set.add(string[i:i+2])
    return aba_set

def aba_bab(string: str):
    inner = []
    while '[' in string:
        left_ind = string.find('[')
        right_ind = string.find(']') + 1
        inner.append(string[(left_ind + 1):(right_ind - 1)])
        string = string[:left_ind] + ' ' +  string[right_ind:]
    outer = string.split(' ')

    aba_set = set()
    for string in outer:
        aba_set = aba_set.union(get_aba(string))

    for aba in aba_set:
        bab = aba[1] + aba[0] + aba[1]
        for string in inner:
            if bab in string:
                return True
    return False
    
count = 0
for line in lines:
    if aba_bab(line.strip()):
        count += 1

print(count)
    