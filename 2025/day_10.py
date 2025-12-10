import z3

data = open(0).read().strip()
lines = data.split("\n")

def parse(line):
    line = line.split()
    lights = [x == "#" for x in line[0].strip("[]")]
    buttons = []
    for button in line[1:-1]:
        buttons.append([int(x) for x in button.strip("()").split(",")])
    joltages = [int(x) for x in line[-1].strip("{}").split(",")]
    return lights, buttons, joltages

p1 = p2 = 0
for line in lines:
    lights, buttons, joltages = parse(line)
    n = len(buttons)

    # part 1
    bitmasks = []
    for b in buttons:
        mask = 0
        for i in b:
            mask ^= 1 << i
        bitmasks.append(mask)
    goal = 0
    for i, x in enumerate(lights):
        if x:
            goal |= 1 << i
    t = 10 ** 9
    for mask in range(1 << n):
        x = mask.bit_count()
        cand = 0
        i = 0
        while mask:
            if mask & 1:
                cand ^= bitmasks[i]
            mask >>= 1
            i += 1
        if cand == goal:
            t = min(t, x)
    p1 += t

    # part 2
    opt = z3.Optimize()
    vars = {str(b): z3.Int(str(b)) for b in buttons}
    opt.minimize(sum(vars.values()))
    for var in vars.values():
        opt.add(var >= 0)
    for i, j in enumerate(joltages):
        active = [vars[str(b)] for b in buttons if i in b]
        eq = sum(active) == j
        opt.add(eq)
    opt.check()
    p2 += opt.model().evaluate(sum(vars.values())).as_long()
            
print("p1 =", p1)
print("p2 =", p2)