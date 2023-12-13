data = open(0).read().strip()
patterns = data.split("\n\n")


def vertical(grid, rows, cols, part2):
    res = 0
    for c in range(cols - 1):
        wrong = 0
        for cc in range(cols):
            left = c - cc
            right = c + cc + 1
            if 0 <= left < right < cols:
                left_col = [grid[r][left] for r in range(rows)]
                right_col = [grid[r][right] for r in range(rows)]
                wrong += rows - [ord(x) - ord(y) for x, y in zip(left_col, right_col)].count(0)
                if not part2 and wrong or (part2 and wrong > 1):
                    break
        if wrong == (1 if part2 else 0):
            res += c + 1
    return res


def horizontal(grid, rows, part2):
    res = 0
    for r in range(rows - 1):
        wrong = 0
        for rr in range(rows):
            above = r - rr
            under = r + rr + 1
            if 0 <= above < under < rows:
                wrong += cols - [ord(x) - ord(y) for x, y in zip(grid[above], grid[under])].count(0)
                if not part2 and wrong or (part2 and wrong > 1):
                    break
        if wrong == (1 if part2 else 0):
            res += r + 1
    return 100 * res

p1 = 0
p2 = 0
for pattern in patterns:
    grid = [[x for x in line] for line in pattern.split("\n")]
    rows = len(grid)
    cols = len(grid[0])
    p1 += vertical(grid, rows, cols, False)
    p1 += horizontal(grid, rows, False)
    p2 += vertical(grid, rows, cols, True)
    p2 += horizontal(grid, rows, True)

print("p1 =", p1)
print("p2 =", p2)
