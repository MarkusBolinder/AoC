data = open(0).read().strip()
colors, patterns = data.split("\n\n")
colors = colors.split(", ")
patterns = patterns.split("\n")

seen = {}
def solve(pattern, colors):
    if pattern in seen:
        return seen[pattern]
    res = 0
    if pattern == "":
        res = 1
    for color in colors:
        if pattern.startswith(color):
            res += solve(pattern[len(color):], colors)
    seen[pattern] = res
    return res

p1 = 0
p2 = 0
for pattern in patterns:
    t = solve(pattern, colors)
    if t > 0:
        p1 += 1
    p2 += t

print("p1 =", p1)
print("p2 =", p2)
