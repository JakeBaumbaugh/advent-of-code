import math

def get_factors(num):
    factors = set()
    for i in range(1, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            if i >= num / 50:
                factors.add(i)
            if num // i >= num / 50:
                factors.add(num // i)
    factors.add(num)
    return(factors)

def calc_presents(house):
    return sum([11 * factor for factor in get_factors(house)])

print(get_factors(2636364))

house = 1
while True:
    presents = calc_presents(house)
    if presents >= 29000000:
        break
    house += 1
    if house % 1000 == 0:
        print('current house', house, 'with', presents, 'presents')

print(house)