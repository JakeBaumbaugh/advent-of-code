arr1 = []
arr2 = []
with open('input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    parts = line.split()
    arr1.append(int(parts[0]))
    arr2.append(int(parts[1]))

counts = {}
for num in arr2:
    counts[num] = counts[num] + 1 if num in counts else 1

sum = 0
for num in arr1:
    sum += num * (counts[num] if num in counts else 0)
print(sum)