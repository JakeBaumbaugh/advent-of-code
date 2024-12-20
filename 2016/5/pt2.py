import hashlib

def md5(input: str):
    return hashlib.md5(input.encode()).digest().hex()
def valid_index(char: str):
    return char in '01234567'
def full(arr: list):
    for s in arr:
        if s == '':
            return False
    return True
def calc_password(door: str):
    password = ['', '', '', '', '', '', '', '']
    counter = 0
    while not full(password):
        hash = md5(door + str(counter))
        if hash.startswith('00000') and valid_index(hash[5]) and password[int(hash[5])] == '':
            password[int(hash[5])] = hash[6]
            print(','.join(password))
        counter += 1
    return ''.join(password)

print(calc_password('uqwqemis'))