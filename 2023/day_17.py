import heapq

data = open(0).read().strip()
lines = data.split("\n")

grid = [[int(x) for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

#              down    left     up       right
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def solve(part2):
    pq = []
    pq.append((0, 0, 0, -1, -1))
    distances = {}
    while pq:
        loss, r, c, d, curr = heapq.heappop(pq)
        if not (r, c, d, curr) in distances:
            distances[(r, c, d, curr)] = loss
            for dd, (rr, cc) in enumerate(directions):
                nr = r + rr
                nc = c + cc
                next = curr + 1 if dd == d else 1
                # check if inside grid, not going backwards, and not too far in a straight line (or too short)
                validity = next <= 10 and (dd == d or curr >=4 or curr == -1) if part2 else next <= 3
                if 0 <= nr < rows and 0 <= nc < cols and (dd + 2) % 4 != d and validity:
                    heapq.heappush(pq, (loss + grid[nr][nc], nr, nc, dd, next))
    res = 10 ** 9
    for (r, c, _, curr), loss in distances.items():
        restriction = curr >= 4 if part2 else True
        if r == rows - 1 and c == cols - 1 and restriction:
            res = min(res, loss)
    return res
    
print("p1 =", solve(False))
print("p2 =", solve(True))
