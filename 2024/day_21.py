data = open(0).read().strip()
codes = data.split("\n")

pos = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
pads = [[None, "^", "A"], ["<", "v", ">"]]

dirs = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

def position(t, k):
    if not isinstance(k, str):
        return k
    for r, row in enumerate(t):
        for c, x in enumerate(row):
            if k == x:
                return (r, c)

seen = {}
def solve(s, e, l, max_l):
    # start, end, levels
    k = (s, e, l)
    if k in seen:
        return seen[k]
    
    s = position(pads, s)
    e = position(pads, e)

    d0 = abs(e[0] - s[0]) - 1
    d1 = abs(e[1] - s[1]) - 1
    v = "^" if e[0] < s[0] else "v" if e[0] > s[0] else None
    h = "<" if e[1] < s[1] else ">" if e[1] > s[1] else None

    if l > 0:
        if not h and not v:
            res = solve("A", "A", l - 1, max_l)
        elif not h:
            res = solve("A", v, l - 1, max_l) + d0 * solve(v, v, l - 1, max_l) + solve(v, "A", l - 1, max_l)
        elif not v:
            res = solve("A", h, l - 1, max_l) + d1 * solve(h, h, l - 1, max_l) + solve(h, "A", l - 1, max_l)
        else:
            if (s[1] == 0 and l < max_l) or ((s[1], e[0]) == (0, 3) and l == max_l):
                res = solve("A", h, l - 1, max_l) + d1 * solve(h, h, l - 1, max_l) + solve(h, v, l - 1, max_l) + \
                        d0 * solve(v, v, l - 1, max_l) + solve(v, "A", l - 1, max_l)
            elif (e[1] == 0 and l < max_l) or ((s[0], e[1]) == (3, 0) and l == max_l):
                res = solve("A", v, l - 1, max_l) + d0 * solve(v, v, l - 1, max_l) + solve(v, h, l - 1, max_l) + \
                        d1 * solve(h, h, l - 1, max_l) + solve(h, "A", l - 1, max_l)
            else:
                res = min(
                    solve("A", h, l - 1, max_l) + d1 * solve(h, h, l - 1, max_l) + solve(h, v, l - 1, max_l) + \
                        d0 * solve(v, v, l - 1, max_l) + solve(v, "A", l - 1, max_l),
                    solve("A", v, l - 1, max_l) + d0 * solve(v, v, l - 1, max_l) + solve(v, h, l - 1, max_l) + \
                        d1 * solve(h, h, l - 1, max_l) + solve(h, "A", l - 1, max_l)
                )
    else:
        res = 1

    seen[k] = res
    return res

p1 = 0
p2 = 0
for code in codes:
    n = int(code[:3])
    t1 = t2 = 0
    for sp, ep in zip("A" + code, code):
        sp = position(pos, sp)
        ep = position(pos, ep)
        t1 += solve(sp, ep, 3, 3)
        t2 += solve(sp, ep, 26, 26)
    p1 += n * t1
    p2 += n * t2

print("p1 =", p1)
print("p2 =", p2)
