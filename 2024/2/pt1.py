def is_safe(report):
    nums = [int(level) for level in report.split()]
    if len(nums) == 1:
        return True
    inc_dec = nums[1] > nums[0] # true: inc, false: dec
    for i in range(len(nums) - 1):
        diff = nums[i+1] - nums[i]
        if inc_dec and (diff < 1 or diff > 3):
            return False
        if not inc_dec and (diff > -1 or diff < -3):
            return False
    return True

with open('input.txt', 'r') as file:
    lines = file.readlines()

sum = 0
for line in lines:
    if is_safe(line):
        sum += 1
print(sum)