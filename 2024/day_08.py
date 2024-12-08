from collections import defaultdict

data = open(0).read().strip()
lines = data.split("\n")

grid = [[x for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

antennas = defaultdict(list)

for x in range(rows):
    for y in range(cols):
        if grid[x][y] != ".":
            antennas[grid[x][y]].append((x, y))

p1 = set()
p2 = set()

for x in range(rows):
    for y in range(cols):
        for antenna, positions in antennas.items():
            for x1, y1 in positions:
                for x2, y2 in positions:
                    if (x1, y1) == (x2, y2):
                        continue
                    dx1 = x - x1
                    dy1 = y - y1
                    dx2 = x - x2
                    dy2 = y - y2
                    d1 = abs(dx1) + abs(dy1)
                    d2 = abs(dx2) + abs(dy2)
                    # slopes: k1 = dy1 / dx1 and k2 = dy2 / dx2 => equal if dy1 * dx2 = dx1 * dy2
                    if (d1 == 2 * d2 or d2 == 2 * d1) and (dy1 * dx2 == dx1 * dy2):
                        p1.add((x, y))
                    if (dy1 * dx2 == dx1 * dy2):
                        p2.add((x, y))

print("p1 =", len(p1))
print("p2 =", len(p2))
