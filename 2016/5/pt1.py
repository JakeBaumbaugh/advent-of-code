import hashlib

def md5(input: str):
    return hashlib.md5(input.encode()).digest().hex()

password = ''
counter = 0
while len(password) < 8:
    hash = md5('uqwqemis' + str(counter))
    if hash.startswith('00000'):
        password += hash[5]
        print(password)
    counter += 1
print(password)