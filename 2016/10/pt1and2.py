import re 

with open('input.txt', 'r') as file:
    lines = file.readlines()

class Bot:
    def __init__(self, num, to):
        self.values = []
        self.num = num
        self.to = to
    
    def give(self, val):
        if len(self.values) > 1:
            raise ValueError('cannot give to bot')
        if len(self.values) == 0:
            self.values = [val]
        else:
            curr = self.values[0]
            self.values = [curr, val] if curr < val else [val, curr]
    
    def clear(self):
        self.values = []

    def ready(self):
        return len(self.values) == 2

bots = {}
outputs = {}
give_lines = []

def give(dest, val):
    [type, num] = dest.split(' ')
    num = int(num)
    if type == 'bot':
        bots[num].give(val)
    else:
        outputs[num] = val

for line in lines:
    match = re.match('bot (\\d+) gives low to (.+) and high to (.+)', line)
    if match is not None:
        bot_num = int(match.group(1))
        bots[bot_num] = Bot(bot_num, [match.group(2), match.group(3)])
    else:
        give_lines.append(line)

for line in give_lines:
    match = re.match('value (\\d+) goes to bot (\\d+)', line)
    if match is None:
        raise ValueError('bad line: ' + line)
    bot_num = int(match.group(2))
    bots[bot_num].give(int(match.group(1)))

while True:
    ready_bots = [bot for bot in bots.values() if bot.ready()]
    if len(ready_bots) == 0:
        break
    for bot in ready_bots:
        if bot.values[0] == 17 and bot.values[1] == 61:
            print('bot num ', bot.num)
        give(bot.to[0], bot.values[0])
        give(bot.to[1], bot.values[1])
        bot.clear()

print(outputs[0] * outputs[1] * outputs[2])