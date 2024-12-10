from collections import deque

data = open(0).read().strip()
lines = data.split("\n")

grid = [[int(x) for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

trailheads = []

for i in range(rows):
    for j in  range(cols):
        if grid[i][j] == 0:
            trailheads.append((i, j))

p1 = 0

for x0, y0 in trailheads:
    q = deque()
    q.append((x0, y0))
    seen = set()
    seen.add((x0, y0))
    while q:
        x, y = q.popleft()
        h = grid[x][y]
        if h == 9:
            p1 += 1
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] - h == 1 and (xx, yy) not in seen:
                q.append((xx, yy))
                seen.add((xx, yy))

p2 = 0

for x0, y0 in trailheads:
    q = deque()
    q.append((x0, y0))
    while q:
        x, y = q.popleft()
        h = grid[x][y]
        if h == 9:
            p2 += 1
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] - h == 1:
                q.append((xx, yy))

print("p1 =", p1)
print("p2 =", p2)
