data = open(0).read().strip()
lines = data.split("\n")

grid = [[x for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

def horizontal(G):
    t = 0
    for i in range (rows):
        for j in range(cols - 3):
            hor = "".join(G[i][j:j + 4])
            if hor == "XMAS" or hor == "SAMX":
                t += 1
    return t

def vertical(G):
    t = 0
    for i in range (rows - 3):
        for j in range(cols):
            vert = "".join([G[i + k][j] for k in range(4)])
            if vert == "XMAS" or vert == "SAMX":
                t += 1
    return t

def right_diagonal(G):
    t = 0
    for i in range (rows - 3):
        for j in range(cols - 3):
            diag = "".join([G[i + k][j + k] for k in range(4)])
            if diag == "XMAS" or diag == "SAMX":
                t += 1
    return t

def left_diagonal(G):
    t = 0
    for i in range (3, rows):
        for j in range(cols - 3):
            diag = "".join([G[i - k][j + k] for k in range(4)])
            if diag == "XMAS" or diag == "SAMX":
                t += 1
    return t


def xmas(G):
    t = 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            d1 = "".join([G[i - 1][j - 1], G[i][j], G[i + 1][j + 1]])
            d2 = "".join([G[i - 1][j + 1], G[i][j], G[i + 1][j - 1]])
            if (d1 == "MAS" and d2 == "MAS") or (d1 == "MAS" and d2 == "SAM") or (d1 == "SAM" and d2 == "MAS") or (d1 == "SAM" and d2 == "SAM"):
                t += 1
    return t


p1 = horizontal(grid) + vertical(grid) + right_diagonal(grid) + left_diagonal(grid)
p2 = xmas(grid)

print("p1 =", p1)
print("p2 =", p2)
