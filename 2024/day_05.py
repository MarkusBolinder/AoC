from collections import defaultdict
from functools import cmp_to_key

data = open(0).read().strip()
stuff = data.split("\n\n")
info = stuff[0].split("\n")
queries = stuff[1].split("\n")

before = defaultdict(set)
after = defaultdict(set)

for line in info:
    a, b = map(int, line.split("|"))
    before[b].add(a)
    after[a].add(b)

p1 = 0
p2 = 0

def key(x, y):
    return 1 if x in after[y] else -1 if x in before[y] else 0

for query in queries:
    numbers = list(map(int, query.split(",")))
    n = len(numbers)
    valid = True
    for i in range(n):
        for j in range(n):
            if j < i and numbers[j] in after[numbers[i]]:
                valid = False
            elif j > i and numbers[j] in before[numbers[i]]:
                valid = False
    if valid:
        p1 += numbers[n // 2]
    else:
        numbers.sort(key=cmp_to_key(key))
        p2 += numbers[n // 2]

print("p1 =", p1)
print("p2 =", p2)
