with open('input.txt', 'r') as file:
    lines = file.readlines()
lines = [line[:-1] for line in lines]

def is_valid(total, nums):
    if len(nums) == 1:
        return total == nums[0]
    sum = nums[0] + nums[1]
    prod = nums[0] * nums[1]
    cat = nums[0] * pow(10, len(str(nums[1]))) + nums[1]
    rest_nums = nums[2:]
    return is_valid(total, [sum, *rest_nums]) \
        or is_valid(total, [prod, *rest_nums]) \
        or is_valid(total, [cat, *rest_nums])

sum = 0
for line in lines:
    total = int(line.split(':')[0])
    nums = [int(val) for val in line.split()[1:]]
    if is_valid(total, nums):
        sum += total
print(sum)