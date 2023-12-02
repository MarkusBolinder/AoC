data = open(0).read().strip()
lines = data.split("\n")

p2 = 0
for line in lines:
    line = line.split(": ")[1]
    sets = line.split(";")
    current = {"red" : 0, "blue" : 0, "green" : 0}
    for s in sets:
        s = s.strip().split(",")
        for pair in s:
            pair = pair.strip().split()
            color = pair[1]
            amount = int(pair[0])
            current[color] = max(current[color], amount)
    p2 += current["red"] * current["blue"] * current["green"]

game  = 1
limits = {"red" : 12, "green" : 13, "blue" : 14}
p1 = 0
for line in lines:
    line = line.split(": ")[1]
    sets = line.split(";")
    add = True
    for s in sets:
        s = s.strip().split(", ")
        for pair in s:
            pair = pair.strip().split()
            color = pair[1]
            amount = int(pair[0])
            if amount > limits[color]:
                add = False
                break
        if not add:
            break
    if add:
        p1 += game
    game += 1

print("p1 =", p1, "\np2 =", p2)