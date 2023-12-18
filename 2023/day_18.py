data = open(0).read().strip()
lines = data.split("\n")
actions = []

directions = {"D" : (1, 0), "L" : (0, -1), "U" : (-1, 0), "R" : (0, 1)}
hex_map = {"1" : (1, 0), "2" : (0, -1), "3" : (-1, 0), "0" : (0, 1)}

for line in lines:
    stuff = line.split()
    direction = stuff[0]
    distance = int(stuff[1])
    rgb = stuff[2]
    actions.append((direction, distance, rgb))

v1 = []
v2 = []
pos1 = (0, 0)
pos2 = (0, 0)
# v = vertices, b = boundary
v1.append(pos1)
v2.append(pos2)
b1 = 0
b2 = 0

for d, steps, rgb in actions:
    # part 1
    rr, cc = directions[d]
    pos1 = (pos1[0] + rr * steps, pos1[1] + cc * steps)
    v1.append(pos1)
    b1 += steps
    # part 2
    rgb = rgb.strip("()#")
    hex = int(rgb[:-1], 16)
    dir = rgb[-1]
    rr, cc = hex_map[dir]
    pos2 = (pos2[0] + rr * hex, pos2[1] + cc * hex)
    v2.append(pos2)
    b2 += hex

# shoelace formula, kind of, but also taking the discrete nature of the grid into account
p1 = 0
x0, y0 = v1[-1]
for x1, y1 in v1:
    p1 += (x1 + x0) * (y1 - y0)
    x0, y0 = x1, y1
p1 = abs(p1) // 2 + b1 // 2 + 1

p2 = 0
x0, y0 = v2[-1]
for x1, y1 in v2:
    p2 += (x1 + x0) * (y1 - y0)
    x0, y0 = x1, y1
p2 = abs(p2) // 2 + b2 // 2 + 1

print("p1 =", p1)
print("p2 =", p2)
