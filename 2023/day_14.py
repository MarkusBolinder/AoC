data = open(0).read().strip()
lines = data.split("\n")

grid = [[x for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])


def north(grid, rows, cols):
    for _ in range(rows): # roll until done
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "O":
                    if r - 1 >= 0 and grid[r - 1][c] == ".":
                        grid[r - 1][c] = "O"
                        grid[r][c] = "."
    return grid

def west(grid, rows, cols):
    for r in range(rows):
        for _ in range(cols): # roll until done
            for c in range(cols):
                if grid[r][c] == "O":
                    if c - 1 >= 0 and grid[r][c - 1] == ".":
                        grid[r][c - 1] = "O"
                        grid[r][c] = "."
    return grid

def south(grid, rows, cols):
    for _ in range(rows): # roll until done
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "O":
                    if r + 1 < rows and grid[r + 1][c] == ".":
                        grid[r + 1][c] = "O"
                        grid[r][c] = "."
    return grid

def east(grid, rows, cols):
    for r in range(rows):
        for _ in range(cols): # roll until done
            for c in range(cols):
                if grid[r][c] == "O":
                    if c + 1 < cols and grid[r][c + 1] == ".":
                        grid[r][c + 1] = "O"
                        grid[r][c] = "."
    return grid

def load(grid, rows, cols):
    load = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "O":
                load += rows - r
    return load

def print_grid(grid):
    for row in grid:
        for rock in row:
            print(rock, end="")
        print()


# for part 1
movable = True
while movable:
    moved = False
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "O":
                if r - 1 >= 0 and grid[r - 1][c] == ".":
                    grid[r - 1][c] = "O"
                    grid[r][c] = "."
                    moved = True
    if not moved:
        movable = False

p1 = load(grid, rows, cols)
print("p1 =", p1)


# for part 2
seen = {}

cycles = 10 ** 9
cycle = 0
while cycle < cycles:
    cycle += 1
    for direction in range(4):
        if direction == 0:
            grid = north(grid, rows, cols)
        elif direction == 1:
            grid = west(grid, rows, cols)
        elif direction == 2:
            grid = south(grid, rows, cols)
        elif direction == 3:
            grid = east(grid, rows, cols)
        current_grid = tuple(tuple(rocks) for rocks in grid)
        if current_grid in seen:
            period = cycle - seen[current_grid]
            to_add = (cycles - cycle) // period
            cycle += to_add * period
        seen[current_grid] = cycle
p2 = load(grid, rows, cols)
print("p2 =", p2)
