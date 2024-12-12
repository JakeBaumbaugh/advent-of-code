import re
letters = 'abcdefghjkmnpqrstuvwxyz'

def aabb(password):
    return re.search('.*(.)\\1.*(.)\\2.*', password) is not None
def abc(password):
    ords = [ord(c) for c in password]
    for i in range(6):
        if ords[i] + 1 == ords[i+1] and ords[i+1] + 1 == ords[i+2]:
            return True
    return False
def valid_password(password):
    return aabb(password) and abc(password)
def valid_first_six(password):
    return re.search('.*(.)\\1.*', password[:6]) is not None
    

def inc_letter(letter):
    index = letters.index(letter)
    return letters[(index + 1) % len(letters)]
def inc_password(password: str):
    if password == 'zzzzzzzz':
        return 'aaaaaaaa'
    trimmed_password = password.rstrip('z')
    len_trimmed = len(password) - len(trimmed_password)
    return trimmed_password[:-1] + inc_letter(trimmed_password[-1]) + ('a' * len_trimmed)

password = 'cqjxjnds'
while True:
    if valid_password(password):
        break
    if not valid_first_six(password):
        password = password[:6] + 'zz'
    password = inc_password(password)
print('valid password 1', password)

password = inc_password(password)
while True:
    if valid_password(password):
        break
    if not valid_first_six(password):
        password = password[:6] + 'zz'
    password = inc_password(password)
print('valid password 2', password)