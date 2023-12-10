from collections import deque, defaultdict

data = open(0).read().strip()
lines = data.split("\n")

rows = len(lines)
cols = len(lines[0])

connections = {
    1 : [(-1, 0), (1, 0)], # | pipe
    2 : [(0, -1), (0, 1)], # - pipe
    3 : [(-1, 0), (0, 1)], # L pipe
    4 : [(-1, 0), (0, -1)], # J pipe
    5 : [(0, -1), (1, 0)], # 7 pipe
    6 : [(1, 0), (0, 1)], # F pipe
    7 : [], # S pipe
}

start = (-1, -1)
grid = [[0 for c in range(cols)] for r in range(rows)]
for r in range(rows):
    for c in range(cols):
        pipe = lines[r][c]
        if pipe == "|":
            grid[r][c] = 1
        elif pipe == "-":
            grid[r][c] = 2
        elif pipe == "L":
            grid[r][c] = 3
        elif pipe == "J":
            grid[r][c] = 4
        elif pipe == "7":
            grid[r][c] = 5
        elif pipe == "F":
            grid[r][c] = 6
        elif pipe == "S":
            start = (r, c)
            grid[r][c] = 7

def find_loop(start, grid):
    r, c = start
    n = grid[r - 1][c]
    w = grid[r][c - 1]
    s = grid[r + 1][c]
    e = grid[r][c + 1]
    b1 = b2 = b3 = b4 = False
    if n == 1 or n == 5 or n == 6:
        connections[7].append((-1, 0))
        b1 = True
    if s == 1 or s == 3 or s == 4:
        connections[7].append((1, 0))
        b2 = True
    if w == 2 or w == 3 or w == 6:
        connections[7].append((0, -1))
        b3 = True
    if e == 2 or e == 4 or e == 5:
        connections[7].append((0, 1))
        b4 = True
    if b1 and b2:
        return 1 # S = |
    if b1 and b3:
        return 4 # S = J
    if b1 and b4:
        return 3 # S = L
    if b2 and b3:
        return 5 # S = 7
    if b2 and b4:
        return 6 # S = F
    if b3 and b4:
        return 2 # S = -

start_pipe = find_loop(start, grid)

q = deque()
q.append(start)
distances = defaultdict(lambda: -1)
distances[start] = 0
loop = set()
loop.add(start)
p1 = 0

# bfs
while q:
    current = q.popleft()
    r, c = current
    pipe = grid[r][c]
    next1 = (r + connections[pipe][0][0], c + connections[pipe][0][1])
    next2 = (r + connections[pipe][1][0], c + connections[pipe][1][1])
    t = [next1, next2]
    for n in t:
        if distances[n] == -1:
            distances[n] = distances[current] + 1
            p1 = max(p1, distances[n])
            q.append(n)
            loop.add(n)

# replace all tiles with a 3 x 3 grid
big_rows = 3 * rows
big_cols = 3 * cols
big_grid = [[0 for _ in range(big_cols)] for _ in range(big_rows)]

big_start = (-1, -1)
for r in range(rows):
    for c in range(cols):
        pipe = grid[r][c]
        if (r, c) == start:
            pipe = start_pipe
        mr = 3 * r + 1
        mc = 3 * c + 1
        if pipe == 0:
            continue
        elif pipe == 1:
            # .|.
            # .|.
            # .|.
            big_grid[mr - 1][mc] = 1
            big_grid[mr][mc] = 1
            big_grid[mr + 1][mc] = 1
        elif pipe == 2:
            # ...
            # ---
            # ...
            big_grid[mr][mc - 1] = 2
            big_grid[mr][mc] = 2
            big_grid[mr][mc + 1] = 2
        elif pipe == 3:
            # .|.
            # .L-
            # ...
            big_grid[mr - 1][mc] = 1
            big_grid[mr][mc] = 3
            big_grid[mr][mc + 1] = 2
        elif pipe == 4:
            # .|.
            # -J.
            # ...
            big_grid[mr - 1][mc] = 1
            big_grid[mr][mc] = 4
            big_grid[mr][mc - 1] = 2
        elif pipe == 5:
            # ...
            # -7.
            # .|.
            big_grid[mr][mc - 1] = 2
            big_grid[mr][mc] = 5
            big_grid[mr + 1][mc] = 1
        elif pipe == 6:
            # ...
            # .F-
            # .|.
            big_grid[mr][mc + 1] = 2
            big_grid[mr][mc] = 6
            big_grid[mr + 1][mc] = 1
        if (r, c) == start:
            big_grid[mr][mc] = 7
            big_start = (mr, mc)

q = deque()
big_loop = set()
q.append(big_start)
big_loop.add(big_start)

# bfs for big loop
while q:
    current = q.popleft()
    r, c = current
    pipe = big_grid[r][c]
    next1 = (r + connections[pipe][0][0], c + connections[pipe][0][1])
    next2 = (r + connections[pipe][1][0], c + connections[pipe][1][1])
    t = [next1, next2]
    for n in t:
        if n not in big_loop:
            q.append(n)
            big_loop.add(n)

# do flood fill at every grid point
seen = set()
q = deque()
q.append((0, 0)) # (0, 0) is outside the area that is enclosed by the loop (I guess that is not guaranteed, but whatever)
seen.add((0, 0))
while q:
    r, c = q.popleft()
    for n in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        x, y = n
        if x < 0 or x >= big_rows or y < 0 or y >= big_cols or (x, y) in big_loop or (x, y) in seen:
            continue
        q.append((x, y))
        seen.add((x, y))

# Print the grid transformation nicely, and fill it in
for r in range(rows):
    for c in range(cols):
        print("o", end="") if (r, c) in loop else print(".", end="")
    print()
print()
for _ in range(cols // 2):
    print(" ", end="")
for _ in range(cols // 3):
    print("|", end="")
print()
for _ in range(cols // 2):
    print(" ", end="")
for _ in range(cols // 3):
    print("v", end="")
print("\n")

for r in range(big_rows):
    for c in range(big_cols):
        print("o", end="") if (r, c) in big_loop else print("-", end="") if (r, c) in seen else print(".", end="")
    print()

# I have not proven that this always gives the correct answer, however it feels like it does
p2 = -(-(big_rows * big_cols - 2 * len(big_loop) - len(seen)) // 9)

# For mathematical doubters:
check = 0
bigger_loop = set()
for r, c in big_loop:
    for rr in [-1, 0, 1]:
        for cc in [-1, 0, 1]:
            bigger_loop.add((r + rr, c + cc))

for r in range(big_rows):
    for c in range(big_cols):
        if (r, c) not in seen and (r, c) not in bigger_loop:
            check += 1
check //= 9


assert(check == p2)
print("p1 =", p1)
print("p2 =", p2)