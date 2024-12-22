with open('input.txt', 'r') as file:
    lines = file.readlines()

def mix(a, b):
    return a ^ b
def prune(a):
    return a % 16777216
def next_secret(prev):
    secret = prune(mix(prev, prev * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret

secrets = [int(line.strip()) for line in lines]
# secrets = [1, 10, 100, 2024]
for _ in range(2000):
    secrets = [next_secret(secret) for secret in secrets]
print(sum(secrets))
