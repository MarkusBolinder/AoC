data = open(0).read().strip()
lines = data.split("\n")

p1 = 0
p2 = 0

def max_subseq(line, length):
    n = len(line)
    start = 0
    res = []
    for pos in range(length):
        last = n - (length - pos)
        best = start
        best_num = line[start]
        for j in range(start, last + 1):
            num = line[j]
            if num > best_num:
                best_num = num
                best = j
                if best_num == "9":
                    break
        res.append(best_num)
        start = best + 1
    return int("".join(res))

for line in lines:
    p1 += max_subseq(line, 2)
    p2 += max_subseq(line, 12)

print("p1 =", p1)
print("p2 =", p2)