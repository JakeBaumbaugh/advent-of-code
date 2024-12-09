def is_safe(report):
    if len(report) <= 2:
        return True
    inc_dec = report[1] > report[0] # true: inc, false: dec
    for i in range(len(report) - 1):
        diff = report[i+1] - report[i]
        if inc_dec and (diff < 1 or diff > 3):
            return False
        if not inc_dec and (diff > -1 or diff < -3):
            return False
    return True

def is_line_safe(line):
    report = [int(level) for level in line.split()]
    if is_safe(report):
        return True
    for i in range(len(report)):
        new_report = report.copy()
        new_report.pop(i)
        if is_safe(new_report):
            return True
    return False

with open('input.txt', 'r') as file:
    lines = file.readlines()

sum = 0
for line in lines:
    if is_line_safe(line):
        sum += 1
print(sum)