from collections import deque, defaultdict

data = open(0).read().strip()
lines = data.split("\n")

grid = [[x for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

for line in lines:
    pass

p1 = 0
p2 = 0

seen = set()
for x in range(rows):
    for y in range(cols):
        if (x, y) in seen:
            continue
        area = 0
        perimeter = 0
        sides = 0
        q = deque()
        q.append((x, y))
        boundary = defaultdict(set)
        while q:
            (x, y) = q.popleft()
            if (x, y) in seen:
                continue
            seen.add((x, y))
            area += 1
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                xx, yy = x + dx, y + dy
                if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == grid[x][y]:
                    q.append((xx, yy))
                else:
                    perimeter += 1
                    # for part 2: sides can be determined by adjacency and direction
                    boundary[(dx, dy)].add((x, y))
        p1 += area * perimeter

        for k, v in boundary.items():
            visited = set()
            for x, y in v:
                if (x, y) in visited:
                    continue
                q = deque()
                q.append((x, y))
                sides += 1
                while q:
                    x, y = q.popleft()
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        xx, yy = x + dx, y + dy
                        if (xx, yy) in v:
                            q.append((xx, yy))
        p2 += area * sides

print("p1 =", p1)
print("p2 =", p2)
