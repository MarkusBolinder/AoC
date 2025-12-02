numbers = open(0).read().strip(", ").split(",")

p1 = 0
p2 = 0

for ranges in numbers:
    x, y = map(int, ranges.split("-"))
    for z in range(x, y + 1):
        s = str(z)
        n = len(s)
        if s[:n // 2] * 2 == s:
            p1 += z
        for k in range(1, n // 2 + 1):
            if n % k != 0:
                continue
            block = s[:k]
            if block * (n // k) == s:
                p2 += z
                break

print("p1 =", p1)
print("p2 =", p2)