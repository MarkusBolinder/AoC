data = open(0).read().strip()

stones = list(map(int, data.split(" ")))
seen = {}

def f(stone, blinks):
    if (stone, blinks) in seen:
        return seen[(stone, blinks)]
    if blinks == 0:
        res = 1
    elif stone == 0:
        res = f(1, blinks - 1)
    elif (d := len(s := str(stone))) % 2 == 0:
        res = f(int(s[:d // 2]), blinks - 1) + f(int(s[d // 2:]), blinks - 1)
    else:
        res = f(stone * 2024, blinks - 1)
    seen[(stone, blinks)] = res
    return res

p1 = sum([f(stone, 25) for stone in stones])
p2 = sum([f(stone, 75) for stone in stones])

print("p1 =", p1)
print("p2 =", p2)
