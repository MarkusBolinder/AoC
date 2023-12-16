data = open(0).read().strip()
lines = data.split("\n")
grid = [[x for x in line] for line in lines]

splitters = {"." : 0, "/" : 1, "\\" : 2, "|" : 3, "-" : 4}

rows = len(grid)
cols = len(grid[0])

# d: 0 = down, 1 = right, 2 = up, 3 = left
forward_splitter = {0 : 3, 1 : 2, 2 : 1, 3 : 0} # /
backward_splitter = {0 : 1, 1 : 0, 2 : 3, 3 : 2}# \
row_map = {0 : 1, 1 : 0, 2 : -1, 3 : 0}
col_map = {0 : 0, 1 : 1, 2 : 0, 3 : -1}

def next_point(r, c, d):
    row = r + row_map[d]
    col = c + col_map[d]
    return (row, col, d)

def do_some_optics(start, direction):
    seen = set()
    paths = set()
    current = [(*start, direction)]
    while current:
        next = []
        for r, c, d in current:
            if 0 <= r < rows and 0 <= c < cols:
                x = grid[r][c]
                seen.add((r, c))
                if (r, c, d) in paths:
                    continue
                paths.add((r, c, d))
                if x == ".":
                    next.append(next_point(r, c, d))
                elif x == "/":
                    next.append(next_point(r, c, forward_splitter[d]))
                elif x == "\\":
                    next.append(next_point(r, c, backward_splitter[d]))
                elif x == "|":
                    if d == 1 or d == 3:
                        next.append(next_point(r, c, 0))
                        next.append(next_point(r, c, 2))
                    else:
                        next.append(next_point(r, c, d))
                elif x == "-":
                    if d == 0 or d == 2:
                        next.append(next_point(r, c, 1))
                        next.append(next_point(r, c, 3))
                    else:
                        next.append(next_point(r, c, d))
        current = next
    return len(seen)

p1 = do_some_optics((0, 0), 1) # heading right
print("p1 =", p1)
p2 = 0
for c in range(cols):
    p2 = max(p2, do_some_optics((0, c), 0))
    p2 = max(p2, do_some_optics((rows - 1, c), 2))
for r in range(rows):
    p2 = max(p2, do_some_optics((r, 0), 1))
    p2 = max(p2, do_some_optics((r, cols - 1), 3))
print("p2 =", p2)
