def sq(num):
    return num * (num + 1) // 2
def calc_index(point):
    x, y = point
    return sq(x + y - 2) + x
def exp_mod_div(base, exp, mod):
    if exp > 10:
        half_exp = exp // 2
        return exp_mod_div(base, half_exp, mod) * exp_mod_div(base, exp - half_exp, mod) % mod
    return base**exp % mod
def code(index):
    mod = 33554393
    return (exp_mod_div(252533, index-1, mod) * 20151125) % mod

col = 3029
row = 2947
index = calc_index((col, row))
print(code(index))