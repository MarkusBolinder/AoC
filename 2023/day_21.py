from collections import deque

data = open(0).read().strip()
lines = data.split("\n")

grid = [[x for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

start = (-1, -1)
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            start = (r, c)
            grid[r][c] = "."

q = deque()
seen = set()
q.append((*start, 0))

max_steps = 64

while q:
    r, c, steps = q.popleft()
    for rr, cc in directions:
        nr = r + rr
        nc = c + cc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#" and steps < max_steps and (nr, nc, steps + 1) not in seen:
            q.append((nr, nc, steps + 1))
            seen.add((nr, nc, steps + 1))

p1 = 0
for _, _, steps in seen:
    if steps == max_steps:
        p1 += 1



# part 2
        
fast_walks = {}

def walk_faster(steps, max_steps, both):
    state = (steps, max_steps, both)
    if state in fast_walks:
        return fast_walks[state]
    length = rows
    walkable_grids = (max_steps - steps) // length # rows == cols (square grid)
    walk = 0
    # for a given boundary point we can walk indefinitely in the normal direction, until we run out of steps
    for s in range(1, walkable_grids + 1):
        res = steps + s * length
        if res <= max_steps and res % 2 == max_steps % 2:
            walk += s + 1 if both else 1
    fast_walks[state] = walk
    return walk


cache = {}
q = deque()
q.append((*start, 0, 0, 0)) # keep track of actual grid points by placing the grids in a grid of their own
while q:
    r, c, steps, gr, gc = q.popleft()
    if r >= rows:
        gr += 1
        r -= rows
    elif r < 0:
        gr -= 1
        r += rows
    if c >= cols:
        gc += 1
        c -= cols
    elif c < 0:
        gc -= 1
        c += cols
    if grid[r][c] != "#" and (r, c, gr, gc) not in cache and abs(gr) < 6 and abs(gc) < 6: # 6 is good enough, could probably be stricter
        cache[(r, c, gr, gc)] = steps
        for rr, cc in directions:
            nr = r + rr
            nc = c + cc
            q.append((nr, nc, steps + 1, gr, gc))

max_steps = 26501365

p2 = 0
# assume there is a lot of repetitions so that we can look in the closest grids and extrapolate
arbitrary_limit = 4
for r in range(rows):
    for c in range(cols):
        if not (r, c, 0, 0) in cache:
            continue
        # look in a small area around starting grid
        grids = [(gr, gc) for gc in range(-arbitrary_limit, arbitrary_limit + 1) for gr in range(-arbitrary_limit, arbitrary_limit + 1)]
        for gr, gc in grids:
            steps = cache[(r, c, gr, gc)]
            # all reachable points must have the same parity as the maximum number of steps
            if steps <= max_steps and steps % 2 == max_steps % 2:
                p2 += 1
            if abs(gr) == arbitrary_limit and abs(gc) == arbitrary_limit:
                # at corner => more possibilities (represented by True)
                p2 += walk_faster(steps, max_steps, True)
            elif abs(gr) == arbitrary_limit or abs(gc) == arbitrary_limit:
                p2 += walk_faster(steps, max_steps, False)

print("p1 =", p1)
print("p2 =", p2)
