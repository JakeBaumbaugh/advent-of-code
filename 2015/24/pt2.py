with open('input.txt', 'r') as file:
    lines = file.readlines()
presents = [int(line.strip()) for line in lines]
target = sum(presents) // 4

def copy_sleigh(sleigh):
    return [sleigh[0].copy(), sleigh[1].copy(), sleigh[2].copy()]
def sleigh_score(sleigh):
    product = 1
    for present in sleigh[0]:
        product *= present
    return product

class Sleigh:
    def __init__(self):
        self.sets = [set(), set(), set(), set()]
    
    def copy(self):
        sleigh = Sleigh()
        sleigh.sets = [s.copy() for s in self.sets]
        return sleigh
    
    def score(self):
        product = 1
        for present in self.sets[0]:
            product *= present
        return product
    
    def indices_can_add(self, present):
        return [index for index in range(len(self.sets)) if sum(self.sets[index]) + present <= target]
    
    def add_present(self, present, index):
        sleigh = self.copy()
        sleigh.sets[index].add(present)
        return sleigh
    
best_sleigh = None
def check_best_sleigh(sleigh: Sleigh):
    global best_sleigh
    len_sleigh = len(sleigh.sets[0])
    len_best_sleigh = 999999 if best_sleigh is None else len(best_sleigh.sets[0])
    if len_sleigh < len_best_sleigh or (len_sleigh == len_best_sleigh and sleigh.score() < best_sleigh.score()):
        best_sleigh = sleigh
def add_all(sleigh: Sleigh, presents):
    # print(sleigh.sets)
    global best_sleigh
    if len(presents) == 0:
        check_best_sleigh(sleigh)
        print(sleigh.score(), sleigh.sets)
        return
    if best_sleigh is not None and sleigh.score() >= best_sleigh.score():
        # print('sleigh score worse than best sleigh score', best_sleigh.score())
        return
    presents = presents.copy()
    present = presents.pop()
    for index in sleigh.indices_can_add(present):
        add_all(sleigh.add_present(present, index), presents)

add_all(Sleigh(), presents)
print(best_sleigh.score)