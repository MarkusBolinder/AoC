from z3 import *

data = open(0).read().strip()
lines = data.split("\n")

velocities = []
positions = []

for line in lines:
    stuff = line.split(" @ ")
    px, py, pz = map(int, stuff[0].split(", "))
    vx, vy, vz = map(int, stuff[1].split(", "))
    velocities.append((vx, vy, vz))
    positions.append((px, py, pz))

n = len(positions)

p1 = 0

low = 200_000_000_000_000 if len(lines) > 10 else 7
high = 400_000_000_000_000 if len(lines) > 10 else 27

for i in range(n):
    x0, y0, z0 = positions[i]
    vx0, vy0, vz0 = velocities[i]
    for j in range(i + 1, n):
        x1, y1, z1 = positions[j]
        vx1, vy1, vz1 = velocities[j]
        det = vy1 * vx0 - vx1 * vy0
        if det == 0:
            continue
        #sz = - ((z1 - z0) * vx0 - (x1 - x0) * vz0) / (vz1 * vx0 - vx1 * vz0)
        sy = - ((y1 - y0) * vx0 - (x1 - x0) * vy0) / det
        ty = (x1 - x0 + sy * vx1) / vx0
        if sy < 0 or ty < 0:
            continue
        x = x1 + sy * vx1
        y = y1 + sy * vy1
        z = z1 + sy * vz1
        if low <= x <= high and low <= y <= high:
            p1 += 1

print("p1 =", p1)

# use z3 for part 2
x0, y0, z0 = Int("x0"), Int("y0"), Int("z0")
vx0, vy0, vz0 = Int("vx0"), Int("vy0"), Int("vz0")
t = [Int(f't_{i}') for i in range(n)]

solver = Solver()
for i in range(n):
    x, y, z = positions[i]
    vx, vy, vz = velocities[i]
    solver.add(x0 + vx0 * t[i] == x + vx * t[i])
    solver.add(y0 + vy0 * t[i] == y + vy * t[i])
    solver.add(z0 + vz0 * t[i] == z + vz * t[i])

solver.check()

model = solver.model()
p2 = model.eval(x0 + y0 + z0)
print("p2 =", p2)


'''
math:

x = x0 + t * vx0
y = y0 + t * vy0

x = x1 + t * vx1
y = y1 + t * vy1

x0 + t * vx0 = x1 + s * vx1
y0 + t * vy0 = y1 + s * vy1
z0 + t * vz0 = z1 + s * vz1

=>

t * vx0 - s * vx1 = x1 - x0
t * vy0 - s * vy1 = y1 - y0
t * vz0 - s * vz1 = z1 - z0

=>

t * vx0 - s * vx1                     =  x1 - x0
        - s * (vy1 * vx0 - vx1 * vy0) = (y1 - y0) * vx0 - (x1 - x0) * vy0
        - s * (vz1 * vx0 - vx1 * vz0) = (z1 - z0) * vx0 - (x1 - x0) * vz0

=>

t * vx0 - s * vx1 =     x1 - x0
                s = - ((y1 - y0) * vx0 - (x1 - x0) * vy0) / (vy1 * vx0 - vx1 * vy0)
                s = - ((z1 - z0) * vx0 - (x1 - x0) * vz0) / (vz1 * vx0 - vx1 * vz0)

=>

t = (x1 - x0 + s * vx1) / vx0
s = - ((y1 - y0) * vx0 - (x1 - x0) * vy0) / (vy1 * vx0 - vx1 * vy0)
'''
