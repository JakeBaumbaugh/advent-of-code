with open('input.txt', 'r') as file:
    lines = file.readlines()
containers = [int(line) for line in lines]
liters = 150

def n_sum(sum, in_nums):
    out_nums = []
    if len(in_nums) == 0:
        return []
    if in_nums[0] == sum:
        return [[in_nums[0]], *n_sum(sum, in_nums[1:])]
    if in_nums[0] > sum:
        return [*n_sum(sum, in_nums[1:])]
    # in_nums[0] < sum:
    return [*n_sum(sum, in_nums[1:]), *[[in_nums[0], *nums] for nums in n_sum(sum - in_nums[0], in_nums[1:])]]

combinations = n_sum(liters, containers)
min_len = len(min(combinations, key=lambda combination : len(combination)))
small_combinations = [c for c in combinations if len(c) == min_len]
print(len(small_combinations))
