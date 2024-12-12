import re

with open('input.txt', 'r') as file:
    lines = file.readlines()

happiness_dict = {}
for line in lines:
    match = re.search('(.+) would (.+) (\d+) happiness units by sitting next to (.+)\.', line)
    first_name = match.group(1)
    second_name = match.group(4)
    happiness = int(match.group(3)) * (1 if match.group(2) == 'gain' else -1)
    if first_name in happiness_dict:
        happiness_dict[first_name][second_name] = happiness
    else:
        happiness_dict[first_name] = {second_name: happiness}

def all_reorders(list):
    if len(list) <= 1:
        return [list]
    sub_reorders = all_reorders(list[:-1])
    insert = list[-1]
    reorders = []
    for sub_reorder in sub_reorders:
        for i in range(len(sub_reorder) + 1):
            reorders.append([*sub_reorder[:i], insert, *sub_reorder[i:]])
    return reorders

def calc_happiness(names):
    sum = 0
    for i in range(len(names)):
        name_1 = names[i]
        name_2 = names[(i + 1) % len(names)]
        sum += happiness_dict[name_1][name_2] + happiness_dict[name_2][name_1]
    return sum

names = [name for name in happiness_dict.keys()]
name_orders = all_reorders(names)
max_happiness = -1000000
for order in name_orders:
    max_happiness = max(max_happiness, calc_happiness(order))
print(max_happiness)