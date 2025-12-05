intervals, ids = open(0).read().strip().split("\n\n")

intervals = sorted([tuple(map(int, interval.strip().split("-"))) for interval in intervals.split("\n")])
ids = [int(id.strip()) for id in ids.split("\n")]

x0, y0 = intervals[0]
t = []

for x, y in intervals[1:]:
    if x <= y0:
        y0 = max(y, y0)
    else:
        t.append((x0, y0))
        x0, y0 = x, y
t.append((x0, y0))

p1 = 0
p2 = 0

for id in ids:
    for x, y in t:
        if x <= id <= y:
            p1 += 1
            break

for x, y in t:
    p2 += y - x + 1

print("p1 =", p1)
print("p2 =", p2)



