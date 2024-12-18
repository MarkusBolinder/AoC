from collections import deque

data = open(0).read().strip()
lines = data.split("\n")

coords = []
for line in lines:
    coords.append(tuple(map(int, line.split(","))))

n = 71
grid = [["." for _ in range(n)] for _ in range(n)]

for x, y in coords[:1024]:
    grid[y][x] = "#"

seen = set()
q = deque()
start = (0, 0, 0)
end = (n - 1, n - 1)
q.append(start)
p1 = -1
while q:
    x, y, d = q.popleft()
    if (x, y) == end:
        p1 = d
        break
    if (x, y) in seen:
        continue
    seen.add((x, y))
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[ny][nx] != "#":
            q.append((nx, ny, d + 1))

# part 2
grid = [["." for _ in range(n)] for _ in range(n)]
p2 = ""

for i, (x, y) in enumerate(coords):
    grid[y][x] = "#"
    x0, y0 = x, y
    seen = set()
    q = deque()
    start = (0, 0, 0)
    end = (n - 1, n - 1)
    q.append(start)
    ok = False
    while q:
        x, y, d = q.popleft()
        if (x, y) == end:
            ok = True
            break
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[ny][nx] != "#":
                q.append((nx, ny, d + 1))
    if not ok:
        p2 = f"{x0},{y0}"
        break

print("p1 =", p1)
print("p2 =", p2)
