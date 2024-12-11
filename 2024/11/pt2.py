class Stone:
    def __init__(self, num, count):
        self.num = num
        self.count = count
    
    def get_next_stones(self):
        if stone.num == 0:
            return [Stone(1, self.count)]
        str_stone_num = str(stone.num)
        if len(str_stone_num) % 2 == 0:
            mid = len(str_stone_num) // 2
            return [Stone(int(str_stone_num[:mid]), self.count), Stone(int(str_stone_num[mid:]), self.count)]
        return [Stone(self.num * 2024, self.count)]

def get_stone_count(stones):
    stone_count = {}
    for stone in stones:
        if stone.num in stone_count:
            stone_count[stone.num] += stone.count
        else:
            stone_count[stone.num] = stone.count
    return stone_count

with open('input.txt', 'r') as file:
    line = file.readline()[:-1]
stones = [Stone(int(num), 1) for num in line.split()]

for i in range(75):
    new_stones = []
    for stone in stones:
        new_stones.extend(stone.get_next_stones())
    stone_counts = get_stone_count(new_stones)
    stones = [Stone(num, stone_counts[num]) for num in stone_counts]

total_count = 0
for stone in stones:
    total_count += stone.count
print(total_count)    