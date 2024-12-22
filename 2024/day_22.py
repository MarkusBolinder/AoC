from collections import defaultdict

data = open(0).read().strip()
numbers = list(map(int, data.split("\n")))

mix = lambda x, y: x ^ y

prune = lambda x: x % 16777216

def generate(x):
    res = [x]
    for _ in range(2000):
        x = prune(mix(x * 64, x))
        x = prune(mix(x // 32, x))
        x = prune(mix(x * 2048, x))
        res.append(x)
    return res

p1 = 0
p2 = defaultdict(int)
for x in numbers:
    s = generate(x)
    p1 += s[-1]
    s = [y % 10 for y in s]
    diff = [s[i + 1] - s[i] for i in range(len(s) - 1)]
    seen = {}
    for i in range(len(diff) - 3):
        seq = tuple(diff[i:i + 4])
        if seq in seen:
            continue
        seen[seq] = s[i + 4]
    for seq, price in seen.items():
        p2[seq] += price

p2 = max(p2.values())

print("p1 =", p1)
print("p2 =", p2)
