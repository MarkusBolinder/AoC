from heapq import heappop, heappush

data = open(0).read().strip()
grid = data.split("\n")
rows, cols = len(grid), len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            start = (r, c)
        elif grid[r][c] == "E":
            end = (r, c)

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left

def dijkstra(start, dirs, grid):
    rows, cols = len(grid), len(grid[0])
    q = []
    seen = set()
    scores = {}
    for s in start:
        heappush(q, s)

    while q:
        score, d, r, c = heappop(q)
        if (r, c, d) not in scores:
            scores[(r, c, d)] = score
        if (r, c, d) in seen:
            continue
        seen.add((r, c, d))
        dr, dc = dirs[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
            heappush(q, (score + 1, d, nr, nc))
        heappush(q, (score + 1000, (d + 1) % 4, r, c))
        heappush(q, (score + 1000, (d + 3) % 4, r, c))

    return scores

forwards = dijkstra([(0, 1, *start)], dirs, grid)

# Find the lowest score to reach the endpoint
lowest = min(score for (r, c, _), score in forwards.items() if (r, c) == end)

# backward Dijkstra from end
backwards = dijkstra([(0, d, *end) for d in range(4)], [*dirs[2:], *dirs[:2]], grid)
opt = set()
for r in range(rows):
    for c in range(cols):
        for d in range(4):
            if (
                (r, c, d) in forwards and (r, c, d) in backwards
                and forwards[(r, c, d)] + backwards[(r, c, d)] == lowest
            ):
                opt.add((r, c))

p1 = lowest
p2 = len(opt)

print("p1 =", p1)
print("p2 =", p2)
