data = open(0).read().strip()
lines = data.split("\n")

grid = []

for i, line in enumerate(lines):
    row = list(map(int, line.split()))
    grid.append(row)

def safe(a):
    L = len(a)
    b = a
    if min(a) != a[0]:
        b = b[::-1]
    if sorted(b) != b:
        return False
    for i in range(L - 1):
        j = i + 1
        if not (1 <= abs(a[i] - a[j]) <= 3):
            return False
    return True

p1 = 0

for row in grid:
    p1 += 1 if safe(row) else 0


p2 = 0
cols = len(grid[0])

for row in grid:
    cols = len(row)
    for i in range(cols):
        r = [x for j, x in enumerate(row) if j != i]
        if safe(r):
            p2 += 1
            break

print("p1 =", p1)
print("p2 =", p2)
