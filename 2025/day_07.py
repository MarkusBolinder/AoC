data = open(0).read().strip()
lines = data.split("\n")

grid = [[x for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

start = (0, lines[0].index("S"))

p1 = [0]
seen = dict()

def solve(r, c):
    if (r, c) in seen:
        return seen[(r, c)]
    if r == rows - 1:
        t = 1
    elif grid[r][c] == "^":
        p1[0] += 1
        t = solve(r + 1, c - 1) + solve(r + 1, c + 1)
    else:
        t = solve(r + 1, c)
    seen[(r, c)] = t
    return t

p2 = solve(*start)
p1 = p1[0]

print("p1 =", p1)
print("p2 =", p2)