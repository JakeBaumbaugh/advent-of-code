with open('input.txt', 'r') as file:
    lines = file.readlines()

towels = [towel.strip() for towel in lines[0].split(',')]
patterns = [line.strip() for line in lines[2:]]

def get_towel_prefixes(pattern: str, towels):
    return [towel for towel in towels if pattern.startswith(towel)]
def can_make_pattern(pattern, towels):
    if len(pattern) == 0:
        return True
    for towel in get_towel_prefixes(pattern, towels):
        if can_make_pattern(pattern[len(towel):], towels):
            return True
    return False

count = 0
for pattern in patterns:
    if can_make_pattern(pattern, towels):
        print('success', pattern)
        count += 1
    else:
        print('fail')
print(count)