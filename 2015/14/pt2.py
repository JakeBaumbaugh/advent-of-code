import re

class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time

        self.can_fly_time = fly_time
        self.can_rest_time = 0
        self.dist = 0

    def tick_second(self):
        if self.can_fly_time > 0:
            self.dist += self.speed
            self.can_fly_time -= 1
            if self.can_fly_time == 0:
                self.can_rest_time = self.rest_time
        elif self.can_rest_time > 0:
            self.can_rest_time -= 1
            if self.can_rest_time == 0:
                self.can_fly_time = self.fly_time

with open('input.txt', 'r') as file:
    lines = file.readlines()

seconds = 2503
reindeers = []
for line in lines:
    match = re.search('(.+) can fly (\\d+) km\\/s for (\\d+) seconds, but then must rest for (\\d+) seconds.', line)
    reindeers.append(Reindeer(match.group(1), int(match.group(2)), int(match.group(3)), int(match.group(4))))

points = {reindeer.name : 0 for reindeer in reindeers}
for i in range(seconds):
    for reindeer in reindeers:
        reindeer.tick_second()
    best_reindeer = reindeers[0]
    for reindeer in reindeers:
        if reindeer.dist > best_reindeer.dist:
            best_reindeer = reindeer
    points[best_reindeer.name] += 1

print(points)
max_point = 0
for name in points:
    max_point = max(max_point, points[name])
print(max_point)