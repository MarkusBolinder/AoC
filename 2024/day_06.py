data = open(0).read().strip()
lines = data.split("\n")

grid = [[x for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

start = (-1, -1)
visited = set()

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "^":
            start = (i, j)

x, y = start
d = 0 # 0 = up; 1 = right; 2 = down; 3 = left
while True:
    visited.add((x, y))
    dx, dy = [(-1, 0), (0, 1), (1, 0), (0, -1)][d]
    xx = x + dx
    yy = y + dy
    if not (0 <= xx < rows and 0 <= yy < cols):
        break
    elif grid[xx][yy] == "#":
        d = (d + 1) % 4
    else:
        x = xx
        y = yy

p1 = len(visited)
p2 = 0

for obstacle_x in range(rows):
    for obstacle_y in range(cols):
        x, y = start
        d = 0 # 0 = up; 1 = right; 2 = down; 3 = left
        visited = set()
        while True:
            if (x, y, d) in visited:
                p2 += 1
                break
            visited.add((x, y, d))
            dx, dy = [(-1, 0), (0, 1), (1, 0), (0, -1)][d]
            xx = x + dx
            yy = y + dy
            if not (0 <= xx < rows and 0 <= yy < cols):
                break
            elif grid[xx][yy] == "#" or (xx, yy) == (obstacle_x, obstacle_y):
                d = (d + 1) % 4
            else:
                x = xx
                y = yy

print("p1 =", p1)
print("p2 =", p2)
