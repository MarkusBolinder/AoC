data = open(0).read().strip()
lines = data.split("\n")

grid = [[x for x in line] for line in lines]

def count(grid):
    t = 0
    rows = len(grid)
    cols = len(grid[0])
    movable = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue
            next = 0
            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if (rr, cc) == (0, 0):
                        continue
                    nr = r + rr
                    nc = c + cc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                        next += 1
            if next < 4:
                t += 1
                movable.add((r, c))
    return t, movable

p1, movable = count(grid)
p2 = p1
while movable:
    for r, c in movable:
        grid[r][c] = "."
    t, movable = count(grid)
    p2 += t

print("p1 =", p1)
print("p2 =", p2)