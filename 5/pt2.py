with open('input.txt', 'r') as file:
    lines = file.readlines()

rules = []
prints = []
reading_rules = True
for line in lines:
    if len(line) == 1:
        reading_rules = False
    else:
        (rules if reading_rules else prints).append(line[:-1])

rules = [rule.split('|') for rule in rules]
prints = [print.split(',') for print in prints]

def legal_print(print):
    for rule in rules:
        if rule[0] not in print or rule[1] not in print:
            continue
        first_index = print.index(rule[0])
        second_index = print.index(rule[1])
        if first_index > second_index:
            return False
    return True

def sort_print(p):
    subrules = [rule for rule in rules if rule[0] in p and rule[1] in p]
    firsts = [rule[0] for rule in subrules]
    counts = {}
    for first in firsts:
        counts[first] = counts[first] + 1 if first in counts else 1
    counts = [item for item in counts.items()]
    counts.sort(key = lambda item : item[1], reverse=True)
    return [count[0] for count in counts]

prints = [print for print in prints if not legal_print(print)]
prints = [sort_print(p) for p in prints]
middles = [print[len(print)//2] for print in prints]
sum = 0
for middle in middles:
    sum += int(middle)
print(sum)