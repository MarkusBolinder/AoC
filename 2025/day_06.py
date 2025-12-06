from functools import reduce
import operator

data = open(0).read().strip()
lines = data.split("\n")

grid = [[x for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

def part1(lines):
    rows = []
    for line in lines[:-1]:
        row = list(map(int, line.strip().split()))
        rows.append(row)
    rows.append(lines[-1].strip().split())
    t = 0
    for task in zip(*rows):
        if task[-1] == "+":
            t += sum(task[:-1])
        else:
            t += reduce(operator.mul, task[:-1], 1)
    return t

p2 = 0
left_c = 0
for c in range(cols + 1):
    empty = True
    # always do last one
    if c < cols:
        for r in range(rows):
            if grid[r][c] != " ":
                empty = False
                break
    if empty:
        op = grid[-1][left_c]
        t = 0 if op == "+" else 1
        for right_c in range(c - 1, left_c - 1, -1):
            x = 0
            for rr in range(rows - 1):
                if (y := grid[rr][right_c]) != " ":
                    x = x * 10 + int(y)
            t = t + x if op == "+" else t * x
        p2 += t
        left_c = c + 1

p1 = part1(lines)

print("p1 =", p1)
print("p2 =", p2)