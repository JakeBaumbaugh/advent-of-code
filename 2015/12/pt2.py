import json

with open('input.txt', 'r') as file:
    data = json.load(file)

def get_sum(data):
    if type(data) is int:
        return data
    if type(data) is str or type(data) is bool:
        return 0
    if type(data) is list:
        return sum([get_sum(item) for item in data])
    if type(data) is dict:
        if 'red' in data.values():
            return 0
        return sum([get_sum(item) for item in data.values()])
    raise 'unexpected type ' + type(data)

print(get_sum(data))