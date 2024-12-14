data = open(0).read().strip()
lines = data.split("\n")

grid = [[x for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

robots = []
w = 101
h = 103

for line in lines:
    line = line.split(" ")
    x, y = map(int, line[0].split("=")[1].split(","))
    vx, vy = map(int, line[1].split("=")[1].split(","))
    robots.append((x, y, vx, vy))

for i in range(100):
    robots = [((x + vx) % w, (y + vy) % h, vx, vy) for x, y, vx, vy in robots]

mx, my = w // 2, h // 2
qs = [0, 0, 0, 0]
for x, y, _, _ in robots:
    if x == mx or y == my:
        continue
    if x < mx and y < my:
        qs[0] += 1
    elif x < mx and y >= my:
        qs[1] += 1
    elif x >= mx and y < my:
        qs[2] += 1
    elif x >= mx and y >= my:
        qs[3] += 1

p1 = 1
for count in qs:
    p1 *= count

p2 = 100

tree = [
        "000010000",
        "000111000",
        "001111100",
        "011111110",
        "111111111",
        "000010000",
        "000010000"
    ]

tree = [[int(x) for x in y] for y in tree]

th = len(tree)
tw = len(tree[0])

while True:
    robots = [((x + vx) % w, (y + vy) % h, vx, vy) for x, y, vx, vy in robots]
    p2 += 1
    grid = [[0 for _ in range(w)] for _ in range(h)]
    for x, y, _, _ in robots:
        grid[y][x] = 1

    for y in range(h - th + 1):
        for x in range(w - tw + 1):
            ok = True
            for ty in range(th):
                for tx in range(tw):
                    if tree[ty][tx] == 1 and grid[y + ty][x + tx] == 0:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                print("p1 =", p1)
                print("p2 =", p2)
                exit()
