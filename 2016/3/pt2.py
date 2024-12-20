with open('input.txt', 'r') as file:
    lines = file.readlines()

def valid_triangle(nums):
    nums = sorted(nums)
    return nums[0] + nums[1] > nums[2]

valid = 0
i = 0
while i < len(lines):
    tri_lines = lines[i : (i+3)]
    tri_lines = [line.strip().split() for line in tri_lines]
    if valid_triangle([int(tri_lines[0][0]), int(tri_lines[1][0]), int(tri_lines[2][0])]):
        valid += 1
    if valid_triangle([int(tri_lines[0][1]), int(tri_lines[1][1]), int(tri_lines[2][1])]):
        valid += 1
    if valid_triangle([int(tri_lines[0][2]), int(tri_lines[1][2]), int(tri_lines[2][2])]):
        valid += 1
    i += 3
print(valid)