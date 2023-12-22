from copy import deepcopy

data = open(0).read().strip()
lines = data.split("\n")

grid = [[x for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]


blocks = []
occupied = set()

for line in lines:
    stuff = line.split("~")
    x0, y0, z0 = map(int, stuff[0].split(","))
    x1, y1, z1 = map(int, stuff[1].split(","))
    block = []
    not_x_range = x0 == x1
    not_y_range = y0 == y1
    not_z_range = z0 == z1
    if not_y_range and not_z_range:
        for x in range(x0, x1 + 1):
            block.append((x, y0, z0))
    if not_z_range and not_x_range:
        for y in range(y0, y1 + 1):
            block.append((x0, y, z0))
    if not_x_range and not_y_range:
        for z in range(z0, z1 + 1):
            block.append((x0, y0, z))
    for x, y, z in block:
        occupied.add((x, y, z))
    blocks.append(block)


# make all the blocks fall down
def fall(blocks, occupied, moved, current_block):  
    falling = True
    while falling:
        falling = False
        for i, block in enumerate(blocks):
            if i == current_block:
                continue
            can_fall = True
            for x, y, z in block:
                below = (x, y, z - 1)
                if (below not in block and below in occupied) or z == 1:
                    can_fall = False
            if can_fall:
                if current_block >= 0:
                    moved.add(i)
                for x, y, z in block:
                    occupied.add((x, y, z - 1))
                    occupied.discard((x, y, z))
                blocks[i] = [(x, y, z - 1) for x, y, z in block]
                falling = True

fall(blocks, occupied, None, -1)
original_tower = deepcopy(blocks)
original_volume = deepcopy(occupied)

p1 = 0
p2 = 0
# simulate how many would fall for every disintegrated block
for current_block, block in enumerate(blocks):
    occupied = deepcopy(original_volume)
    blocks = deepcopy(original_tower)
    for x, y, z in block:
        occupied.discard((x, y, z))
    moved = set()
    fall(blocks, occupied, moved, current_block)
    fell = len(moved)
    if fell == 0:
        p1 += 1
    p2 += fell

print("p1 =", p1)
print("p2 =", p2)
