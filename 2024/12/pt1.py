with open('input.txt', 'r') as file:
    lines = file.readlines()
map = [list(line[:-1]) for line in lines]

def get_char(point):
    return map[point[1]][point[0]]
def point_up(point):
    return (point[0], point[1] - 1)
def point_down(point):
    return (point[0], point[1] + 1)
def point_left(point):
    return (point[0] - 1, point[1])
def point_right(point):
    return (point[0] + 1, point[1])
    
class Region:
    def __init__(self, char):
        self.char = char
        self.points = set()

    def add_point(self, point):
        self.points.add(point)
    
    def has_point(self, point):
        return point in self.points

    def area(self):
        return len(self.points)
    
    def perimeter(self):
        perimeter = 0
        for point in self.points:
            if not self.has_point(point_up(point)):
                perimeter += 1
            if not self.has_point(point_down(point)):
                perimeter += 1
            if not self.has_point(point_left(point)):
                perimeter += 1
            if not self.has_point(point_right(point)):
                perimeter += 1
        return perimeter

regions = []
points_visited = set()

def find_region(point):
    for region in regions:
        if region.has_point(point):
            return region
    return None
def point_in_map(point):
    return point[1] >= 0 and point[1] < len(map) and point[0] >= 0 and point[0] < len(map[point[1]])
def visit_point(point):
    char = get_char(point)
    to_visit = set()
    added_to_region = False

    up = point_up(point)
    if point_in_map(up) and get_char(up) == char:
        if up in points_visited:
            find_region(up).add_point(point)
            added_to_region = True
        else:
            to_visit.add(up)

    down = point_down(point)
    if point_in_map(down) and get_char(down) == char:
        if down in points_visited:
            find_region(down).add_point(point)
            added_to_region = True
        else:
            to_visit.add(down)

    left = point_left(point)
    if point_in_map(left) and get_char(left) == char:
        if left in points_visited:
            find_region(left).add_point(point)
            added_to_region = True
        else:
            to_visit.add(left)
        
    right = point_right(point)
    if point_in_map(right) and get_char(right) == char:
        if right in points_visited:
            find_region(right).add_point(point)
            added_to_region = True
        else:
            to_visit.add(right)

    if not added_to_region:
        region = Region(char)
        region.add_point(point)
        regions.append(region)
    
    points_visited.add(point)
    for p in to_visit:
        visit_point(p)

for y in range(len(map)):
    for x in range(len(map[y])):
        point = (x, y)
        if point not in points_visited:
            visit_point(point)
    
prices = [region.area() * region.perimeter() for region in regions]

for i in range(len(regions)):
    region = regions[i]
    print(region.char)
    print(region.points)
    print(region.area(), region.perimeter())
    print(prices[i])
print(sum(prices))
