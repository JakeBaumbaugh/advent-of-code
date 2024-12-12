import re

class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
    
    def get_dist(self, seconds):
        flying = True
        dist = 0
        while seconds > 0:
            if flying:
                if seconds >= self.fly_time:
                    dist += self.speed * self.fly_time
                    seconds -= self.fly_time
                else:
                    dist += self.speed * seconds
                    seconds = 0
            else:
                seconds -= self.rest_time
            flying = not flying
        return dist

with open('input.txt', 'r') as file:
    lines = file.readlines()

max_dist = 0
seconds = 2503
for line in lines:
    match = re.search('(.+) can fly (\\d+) km\\/s for (\\d+) seconds, but then must rest for (\\d+) seconds.', line)
    reindeer = Reindeer(match.group(1), int(match.group(2)), int(match.group(3)), int(match.group(4)))
    max_dist = max(max_dist, reindeer.get_dist(seconds))
print(max_dist)