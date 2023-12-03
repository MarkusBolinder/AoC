data = open(0).read().strip()
lines = data.split("\n")

grid = [[c for c in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

p1 = 0
for r in range(rows):
    x = 0
    part = False
    # just iterating from 0 .. cols - 1 means that if a line ends with a number it isn't counted on that line
    for c in range(cols + 1):
        if c < cols and grid[r][c].isdigit():
            p = grid[r][c]
            x = x * 10 + int(p)
            # check if the current number has an adjacent part
            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if 0 <= r + rr < rows and 0 <= c + cc < cols:
                        p = grid[r + rr][c + cc]
                        if not p.isdigit() and p != '.':
                            part = True
        # if a number has been found, but no part, we want to remove the number stored
        elif x > 0:
            if part:
                p1 += x
                part = False
            x = 0

p2 = 0
t = {}
for r in range(rows):
    gears = set()
    x = 0
    for c in range(cols + 1):
        if c < cols and grid[r][c].isdigit():
            p = grid[r][c]
            x = x * 10 + int(p)
            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if 0 <= r + rr < rows and 0 <= c + cc < cols:
                        p = grid[r + rr][c + cc]
                        if p == '*':
                            gears.add((r + rr, c + cc))
        elif x > 0:
            for gear in gears:
                current = t.get(gear)
                if not current:
                    t[gear] = [x]
                else:
                    t[gear].append(x)
            gears = set()
            x = 0

for x in t.values():
    if len(x) > 1:
        p2 += x[0] * x[1]

print("p1 =", p1, "\np2 =", p2)