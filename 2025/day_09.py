data = open(0).read().strip()
lines = data.split("\n")

points = []
for line in lines:
    points.append(tuple(map(int, line.split(","))))
adjacent = points[1:] + points[:1]

def order(a, b):
    return min(a, b), max(a, b)

def inside(x, y):
    hits = 0
    for (x1, y1), (x2, y2) in zip(points, adjacent):
        min_x, max_x = order(x1, x2)
        min_y, max_y = order(y1, y2)
        # boundary
        if x == x1 == x2 and min_y <= y <= max_y:
            return True
        elif y == y1 == y2 and min_x <= x <= max_x:
            return True
        # raycast
        # k = (y2 - y1) / (x2 - x1)
        # m = y1 - k * x1
        # y < kx + m <=> (y - y1) * (x2 - x1) * sign(x2 - x1) < (y2 - y1) * (x - x1)
        sign = -1 if max_x == x1 else 1
        if min_x <= x < max_x and (y - y1) * (x2 - x1) * sign < (y2 - y1) * (x - x1):
                hits += 1
    return hits % 2 == 1

def valid(x1, y1, x2, y2):
    min_x, max_x = order(x1, x2)
    min_y, max_y = order(y1, y2)
    x_points = set((min_x, max_x))
    y_points = set((min_y, max_y))
    for (x1, y1), (x2, y2) in zip(points, adjacent):
        if x1 == x2 and min_x <= x2 <= max_x:
            x_points.add(x2)
        if y1 == y2 and min_y <= y2 <= max_y:
            y_points.add(y2)
    for y in y_points:
        if not inside(min_x, y) or not inside(max_x, y):
            return False
    for x in x_points:
        if not inside(x, min_y) or not inside(x, max_y):
            return False
    return True

p1 = p2 = 0
for i, (x1, y1) in enumerate(points):
    for x2, y2 in points[i + 1:]:
        dx = abs(x2 - x1) + 1
        dy = abs(y2 - y1) + 1
        area = dx * dy
        p1 = max(p1, area)
        if valid(x1, y1, x2, y2):
            # takes a few minutes
            p2 = max(p2, area)

print("p1 =", p1)
print("p2 =", p2)