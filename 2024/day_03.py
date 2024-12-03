import re

data = open(0).read().strip()
lines = data.split("\n")

pattern = r"mul\((\d+),(\d+)\)"
matches = []

for line in lines:
    matches += re.findall(pattern, line)

p1 = 0
for x, y in matches:
    x, y = int(x), int(y)
    p1 += x * y


pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = []

for line in lines:
    matches += re.findall(pattern, line)

p2 = 0
mul = True
for x in matches:
    if x[0] == "m" and mul:
        x = x[4:-1].split(",")
        a, b = int(x[0]), int(x[1])
        p2 += a * b
    elif x == "do()":
        mul = True
    else:
        mul = False

print("p1 =", p1)
print("p2 =", p2)
