data = open(0).read().strip()
objs = data.split("\n\n")

keys = []
locks = []

for obj in objs:
    if obj[0] == "#":
        locks.append(obj.split("\n"))
    else:
        keys.append(obj.split("\n"))

def f(key, lock):
    X = len(key)
    Y = len(key[0])
    for x in range(X):
        for y in range(Y):
            if key[x][y] == "#" and lock[x][y] == "#":
                return False
    return True

p1 = 0

for key in keys:
    for lock in locks:
        if f(key, lock):
            p1 += 1

print("p1 =", p1)
