with open('input.txt', 'r') as file:
    lines = file.readlines()

connections = {}

def add_connection(c1, c2):
    if c1 not in connections:
        connections[c1] = {c1}
    if c2 not in connections:
        connections[c2] = {c2}
    connections[c1].add(c2)
    connections[c2].add(c1)

for line in lines:
    c1, c2 = line.strip().split('-')
    add_connection(c1, c2)

computers = [k for k in connections]
computer_count = len(computers)

def computers_in_lan(lan):
    return [computers[i] for i in range(len(lan)) if lan[i]]
def len_lan(lan):
    return len([c for c in lan if c])
def password(lan):
    return ','.join(sorted([computers[i] for i in range(len(lan)) if lan[i]]))
def can_add_to_lan(lan, c1):
    lan_computers = computers_in_lan(lan)
    if c1 in lan_computers:
        return False
    for c2 in lan_computers:
        if c2 not in connections[c1]:
            return False
    return True
def is_lan(lan):
    lan_computers = computers_in_lan(lan)
    for c1 in lan_computers:
        for c2 in lan_computers:
            if c1 not in connections[c2] or c2 not in connections[c1]:
                return False
    return True

best_lan = tuple([False] * computer_count)
potential_lans = {best_lan}

while len(potential_lans) > 0:
    next_lans = set()
    # each lan
    for lan in potential_lans:
        # set best lan if better
        if len_lan(lan) > len_lan(best_lan):
            best_lan = lan
        # add next lan for every computer we can add to lan
        for i in range(len(lan)):
            if can_add_to_lan(lan, computers[i]):
                new_lan = tuple(True if j == i else lan[j] for j in range(len(lan)))
                next_lans.add(new_lan)
            # if not lan[i]:
            #     new_lan = tuple(True if j == i else lan[j] for j in range(len(lan)))
            #     if is_lan(new_lan):
            #         next_lans.add(new_lan)
    # print([password(lan) for lan in next_lans])
    potential_lans = next_lans
    print(len(potential_lans), 'lans to check')

print(password(best_lan))
