lines = open(0).read().split("\n")
p2 = []
t = {
     "one" : "1",
     "two" : "2",
     "three" : "3",
     "four" : "4",
     "five" : "5",
     "six" : "6",
     "seven" : "7",
     "eight" : "8",
     "nine" : "9"
     }
for line in lines:
    for k, v in t.items():
        line = line.replace(k, k + v + k)
    b = [x for x in line if x.isdigit()]
    p2.append(int(b[0] + b[-1]))

p1 = []
for line in lines:
    b = [x for x in line if x.isdigit()]
    p1.append(int(b[0] + b[-1]))

print("p1 =", sum(p1))
print("p2 =", sum(p2))