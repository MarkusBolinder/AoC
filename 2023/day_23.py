import sys

data = open(0).read().strip()
lines = data.split("\n")

sys.setrecursionlimit(10 ** 6)


grid = [[x for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

slopes = {"v" : (1, 0), "<" : (0, -1), "^" : (-1, 0), ">" : (0, 1)}

neighbors = {}
seen = set()

def dfs(r, c, part2):
    res = -10 ** 6
    if r == rows - 1:
        return 0
    seen.add((r, c))
    tile = grid[r][c]
    if part2:
        for next, steps in neighbors[(r, c)].items():
            if next in seen:
                continue
            res = max(res, dfs(*next, True) + steps)
    else:
        if tile in slopes:
            rr, cc = slopes[tile]
            next = [(r + rr, c + cc)]
        else: 
            next = [(r + rr, c + cc) for rr, cc in slopes.values()]
        for nr, nc in next:
            if (nr, nc) in seen or grid[nr][nc] == "#":
                continue
            res = max(res, dfs(nr, nc, False) + 1)
    seen.remove((r, c))
    return res

p1 = dfs(0, 1, False)


for r in range(rows):
    for c in range(cols):
        if grid[r][c] != "#":
            neighbor = {}
            for rr, cc in slopes.values():
                nr = r + rr
                nc = c + cc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
                    neighbor[(nr, nc)] = 1
            neighbors[(r, c)] = neighbor

# merge all pathways, leaving only intersections with more than 2 choices where to go, and start/end
more = True
while more:
    more = False
    for (r, c), ns in neighbors.items():
        if len(ns) != 2:
            continue
        n1, n2 = ns
        neighbors[n1][n2] = neighbors[n2][n1] = neighbors[n1][(r, c)] + neighbors[(r, c)][n2]
        del neighbors[(r, c)], neighbors[n2][(r, c)], neighbors[n1][(r, c)]
        more = True
        break

seen = set()

p2 = dfs(0, 1, True)

print("p1 =", p1)
print("p2 =", p2)
