from collections import defaultdict

data = open(0).read().strip()
lines = data.split("\n")

coords = []
for line in lines:
    coords.append(tuple(map(int, line.split(","))))

distances = []
for i, (x1, y1, z1) in enumerate(coords):
    for j, (x2, y2, z2) in enumerate(coords):
        if j <= i:
            continue
        dx, dy, dz = x2 - x1, y2 - y1, z2 - z1
        d = dx ** 2 + dy ** 2 + dz ** 2
        distances.append((d, i, j))
distances.sort()

class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, a):
        p = self.parent
        while p[a] != a:
            p[a] = p[p[a]]
            a = p[a]
        return a
    
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True


uf = UnionFind(n := len(coords))
t = 0
limit = 1000
p1 = p2 = 0

for k, (d, i, j) in enumerate(distances):
    if uf.union(i, j):
        t += 1
        if t == n - 1:
            p2 = coords[i][0] * coords[j][0]
            break
    if k == limit - 1:
        sizes = defaultdict(int)
        for l in range(n):
            sizes[uf.find(l)] += 1
        sizes = sorted(sizes.values(), reverse=True)
        p1 = sizes[0] * sizes[1] * sizes[2]

print("p1 =", p1)
print("p2 =", p2)