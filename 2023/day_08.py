from math import gcd

data = open(0).read().strip()
lines = data.split("\n\n")

steps = lines[0].strip()
mappings = {}
start = []

for line in lines[1].split("\n"):
    stuff = line.split(" = ")
    key = stuff[0]
    value = stuff[1].strip("()").split(", ")
    mappings[key] = value
    if key.endswith("A"):
        start.append(key)

i = 0
current = "AAA"
while current != "ZZZ":
    if steps[i % len(steps)] == "R":
        next = 1
    else:
        next = 0
    current = mappings[current][next]
    i += 1

print("p1 =", i)


def lcm(x):
    lcm = 1
    for xx in x:
        lcm = (xx * lcm) // gcd(xx, lcm)
    return lcm

end = {}
current = [x for x in start]

i = 0
while True:
    next = 1 if steps[i % len(steps)] == "R" else 0
    i += 1
    for j, c in enumerate(current):
        current[j] = mappings[c][next]
        if current[j][-1] == "Z":
            end[current[j]] = i
            if len(end) == len(start):
                print("p2 =", lcm(end.values()))
                exit(0)
