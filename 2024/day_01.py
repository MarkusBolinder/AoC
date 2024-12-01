from collections import Counter

data = open(0).read().strip()
lines = data.split("\n")

left = []
right = []

for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

rc = Counter(right)

p1 = sum([abs(x - y) for x,y in zip(left, right)])

p2 = 0

for x in left:
    p2 += x * rc[x]

print("p1 =", p1)
print("p2 =", p2)
