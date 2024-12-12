reqs = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

def matches_reqs(details: dict):
    for key in details:
        if key == 'cats' or key == 'trees':
            if details[key] <= reqs[key]:
                return False
        elif key == 'pomeranians' or key == 'goldfish':
            if details[key] >= reqs[key]:
                return False
        elif details[key] != reqs[key]:
            return False
    return True

with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    line = line[:-1]
    details = line.split(': ', 1)[1]
    details = details.split(', ')
    details = [detail.split(': ') for detail in details]
    details = {detail[0]: int(detail[1]) for detail in details}
    if matches_reqs(details):
        print(line)