arr1 = []
arr2 = []
with open('input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    parts = line.split()
    arr1.append(int(parts[0]))
    arr2.append(int(parts[1]))

arr1.sort()
arr2.sort()

sum = 0
for (a, b) in zip(arr1, arr2):
    sum += abs(a - b)
print(sum)