with open('input.txt', 'r') as file:
    line = file.readline()[:-1]
stones = [int(num) for num in line.split()]

def get_next_stones(stone):
    if stone == 0:
        return [1]
    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        mid = len(str_stone) // 2
        return [int(str_stone[:mid]), int(str_stone[mid:])]
    return [stone * 2024]

for i in range(25):
    new_stones = []
    for stone in stones:
        new_stones.extend(get_next_stones(stone))
    stones = new_stones
    print(i+1, ':', len(stones))

print(len(stones))
    