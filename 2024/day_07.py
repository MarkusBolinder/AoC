data = open(0).read().strip()
lines = data.split("\n")

p1 = 0
p2 = 0

def ok1(n ,t):
    length = len(t)
    for i in range(2 ** (length - 1)):
        res = t[0]
        for j in range(length - 1):
            op = (i // 2 ** j) % 2
            if op == 0:
                res += t[j + 1]
            elif op == 1:
                res *= t[j + 1]
        if res == n:
            return True
    return False

def ok2(n ,t):
    length = len(t)
    for i in range(3 ** (length - 1)):
        res = t[0]
        for j in range(length - 1):
            op = (i // 3 ** j) % 3
            if op == 0:
                res += t[j + 1]
            elif op == 1:
                res *= t[j + 1]
            elif op == 2:
                res = int(str(res) + str(t[j + 1]))
        if res == n:
            return True
    return False

for line in lines:
    line = line.split(": ")
    n = int(line[0])
    numbers = list(map(int, line[1].split(" ")))
    if ok1(n, numbers):
        p1 += n
    if ok2(n, numbers):
        p2 += n

print("p1 =", p1)
print("p2 =", p2)
