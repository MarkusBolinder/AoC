data = open(0).read().strip()
lines = data.split("\n")

times = list(map(int, lines[0].split(": ")[1].split()))
distances = list(map(int, lines[1].split(": ")[1].split()))
ways = [0] * len(times)

for i, (t, d) in enumerate(zip(times, distances)):
    for tt in range(t):
        if tt * (t - tt) > d:
            ways[i] += 1

p1 = 1
for way in ways:
    p1 *= way

print("p1 =", p1)


p2 = 0
time = int("".join([str(x) for x in times]))
distance = int("".join([str(x) for x in distances]))
for t in range(time):
    if t * (time - t) > distance:
        p2 += 1

print("p2 =", p2)