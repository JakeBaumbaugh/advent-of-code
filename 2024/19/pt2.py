with open('input.txt', 'r') as file:
    lines = file.readlines()

towels = [towel.strip() for towel in lines[0].split(',')]
patterns = [line.strip() for line in lines[2:]]

pattern_mem = {}

def get_towel_prefixes(pattern: str, towels):
    return [towel for towel in towels if pattern.startswith(towel)]
def can_make_pattern(pattern, towels, populate_mem=True):
    if pattern in pattern_mem:
        return pattern_mem[pattern]
    if len(pattern) == 0:
        return 1
    count = 0
    for towel in get_towel_prefixes(pattern, towels):
        count += can_make_pattern(pattern[len(towel):], towels)
    if populate_mem:
        pattern_mem[pattern] = count
    return count

count = 0
for pattern in patterns:
    count += can_make_pattern(pattern, towels)
print(count)