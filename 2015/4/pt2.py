import hashlib

def hash(input: str):
    md5 = hashlib.md5()
    md5.update(input.encode())
    return md5.hexdigest()

print(hash('abcdef609043'))

secret = 'ckczppom'
num = 1
while True:
    if hash(secret + str(num)).startswith('000000'):
        break
    num += 1
    if num % 1_000_000 == 0:
        print("checking num =", num)
print(num)