data = open(0).read().strip()
lines = data.split("\n")
sequences = []

for line in lines:
    sequences.append(list(map(int, line.split())))

p1 = 0
p2 = 0

for s in sequences:
    ns1 = [s]
    ns2 = [s[::-1]]
    i = 0
    c = s
    c2 = c[::-1]
    while c != [0] * len(c):
        ns1.append([c[j + 1] - c[j] for j in range(len(c) - 1)])
        ns2.append([c2[j + 1] - c2[j] for j in range(len(c2) - 1)])
        i += 1
        c = ns1[i]
        c2 = ns2[i]
    for i in range(len(ns1) - 1, -1, -1):
        p1 += ns1[i][-1]
        p2 += ns2[i][-1]

print("p1 =", p1)
print("p2 =", p2)