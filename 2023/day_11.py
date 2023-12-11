data = open(0).read().strip()
lines = data.split("\n")

rows = len(lines)
cols = len(lines[0])
grid = [[0 for _ in range(cols)] for _ in  range(rows)]

empty_rows = []
empty_cols = []
galaxies = []

for r in range(rows):
    for c in range(cols):
        if lines[r][c] == "#":
            grid[r][c] = 1
            galaxies.append((r, c))

for r in range(rows):
    if sum(grid[r]) == 0:
        empty_rows.append(r)

for c in range(c):
    if sum([grid[r][c] for r in range(rows)]) == 0:
        empty_cols.append(c)

def solve(part2):
    ans = 0
    for i, (r, c) in enumerate(galaxies):
        for j in range(i, len(galaxies)):
            gr, gc = galaxies[j]
            d = abs(r - gr) + abs(c - gc)
            for er in empty_rows:
                if er in range(min(gr, r), max(gr, r)):
                    d += 1 if not part2 else int(1e6 - 1)
            for ec in empty_cols:
                if ec in range(min(gc, c), max(gc, c)):
                    d += 1 if not part2 else int(1e6 - 1)
            ans += d
    return ans

print("p1 =", solve(False))
print("p2 =", solve(True))
