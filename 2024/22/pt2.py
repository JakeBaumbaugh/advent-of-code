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

def find_subsequence(sequence, subsequence):
    for start in range(len(sequence) - len(subsequence) + 1):
        end = start + len(subsequence)
        if sequence[start:end] == subsequence:
            return start
    return -1
def valid_sequence(seq):
    return abs(sum(seq[0:2])) < 10 and abs(sum(seq[1:3])) < 10 and abs(sum(seq[2:4])) < 10 \
        and abs(sum(seq[0:3])) < 10 and abs(sum(seq[1:4])) < 10 \
        and abs(sum(seq[0:4])) < 10

initials = [int(line.strip()) for line in lines]
bananas = []
for initial in initials:
    secret = initial
    sequence = [secret % 10]
    for _ in range(2000):
        secret = next_secret(secret)
        sequence.append(secret % 10)
    bananas.append(sequence)

change_counts = {}
def add_change_count(change):
    if change in change_counts:
        change_counts[change] += 1
    else:
        change_counts[change] = 1
changes = []
for monkey in bananas:
    sequence = []
    for i in range(len(monkey) - 1):
        sequence.append(monkey[i+1] - monkey[i])
        if i >= 3:
            add_change_count((sequence[-3], sequence[-2], sequence[-1], sequence[0]))
    changes.append(sequence)

sequences = [seq for seq in change_counts.keys()]
sequences.sort(key=lambda seq : change_counts[seq], reverse=True)

best_bananas = 0
for target in sequences:
    print('testing sequence', target)
    banana_total = 0
    for index in range(len(changes)):
        if banana_total + 9 * (len(changes) - index) < best_bananas:
            # cannot reach best
            break
        target_index = find_subsequence(changes[index], [c for c in target])
        if target_index != -1:
            banana_total += bananas[index][target_index + 4]
            continue
    if banana_total > best_bananas:
        print('total', banana_total, 'for sequence', target)
        best_bananas = banana_total
print(best_bananas)
