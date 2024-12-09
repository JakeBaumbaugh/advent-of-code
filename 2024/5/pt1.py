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

prints = [print for print in prints if legal_print(print)]
middles = [print[len(print)//2] for print in prints]
sum = 0
for middle in middles:
    sum += int(middle)
print(sum)