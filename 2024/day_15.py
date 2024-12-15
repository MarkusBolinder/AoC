from collections import deque

data = open(0).read().strip()

grid, moves = data.split("\n\n")
grid = grid.split("\n")
moves = "".join(moves.split("\n"))

def p1(grid):
    rows = len(grid)
    cols = len(grid[0])
    grid = [[grid[x][y] for y in range(cols)] for x in range(rows)]

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "@":
                x0, y0 = x, y
                grid[x][y] = "."

    x, y = x0, y0
    for move in moves:
        dx, dy = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}[move]
        nx, ny = x + dx, y + dy
        if grid[nx][ny] == "#":
            continue
        elif grid[nx][ny] == ".":
            x, y = nx, ny
        elif grid[nx][ny] == "O":
            seen = set()
            q = deque()
            q.append((x, y))
            pushable = True
            while q:
                nx, ny = q.popleft()
                if (nx, ny) in seen:
                    continue
                seen.add((nx, ny))
                lx, ly = nx + dx, ny + dy
                if grid[lx][ly] == "#":
                    pushable = False
                    break
                elif grid[lx][ly] == "O":
                    q.append((lx, ly))
            if not pushable:
                continue
            while seen:
                for nx, ny in sorted(seen):
                    lx, ly = nx + dx, ny + dy
                    if (lx, ly) not in seen:
                        grid[lx][ly] = grid[nx][ny]
                        grid[nx][ny] = "."
                        seen.remove((nx, ny))
            x = x + dx
            y = y + dy

    res = 0
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "O":
                res += 100 * x + y 
    return res

def p2(grid):
    rows = len(grid)
    cols = len(grid[0])
    grid = [[grid[x][y] for y in range(cols)] for x in range(rows)]

    grid = [[y for y in "".join([{"#": "##", "O": "[]", ".": "..", "@": "@."}[y] for y in x])] for x in grid]
    cols = len(grid[0])

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "@":
                x0, y0 = x, y
                grid[x][y] = "."

    x, y = x0, y0
    for move in moves:
        dx, dy = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}[move]
        nx, ny = x + dx, y + dy
        if grid[nx][ny] == "#":
            continue
        elif grid[nx][ny] == ".":
            x, y = nx, ny
        elif grid[nx][ny] in ["[", "]"]:
            seen = set()
            q = deque()
            q.append((x, y))
            pushable = True
            while q:
                nx, ny = q.popleft()
                if (nx, ny) in seen:
                    continue
                seen.add((nx, ny))
                lx, ly = nx + dx, ny + dy
                if grid[lx][ly] == "#":
                    pushable = False
                    break
                elif grid[lx][ly] == "[":
                    q.extend([(lx, ly), (lx, ly + 1)])
                elif grid[lx][ly] == "]":
                    q.extend([(lx, ly), (lx, ly - 1)])
            if not pushable:
                continue
            while seen:
                for nx, ny in sorted(seen):
                    lx, ly = nx + dx, ny + dy
                    if (lx, ly) not in seen:
                        grid[lx][ly] = grid[nx][ny]
                        grid[nx][ny] = "."
                        seen.remove((nx, ny))
            x = x + dx
            y = y + dy

    res = 0
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "[":
                res += 100 * x + y 
    return res

print("p1 =", p1(grid))
print("p2 =", p2(grid))
