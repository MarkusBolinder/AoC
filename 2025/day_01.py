data = open(0).read().strip()
lines = data.split("\n")

grid = [[x for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

t = 50
p1 = 0
p2 = 0

for line in lines:
    a, x = line[0], int(line[1:])
    for _ in range(x):
        if a == "L":
            t = (t - 1) % 100
        else:
            t = (t + 1) % 100
        if t == 0:
            p2 += 1
    if t == 0:
        p1 += 1

print("p1 =", p1)
print("p1 =", p2)