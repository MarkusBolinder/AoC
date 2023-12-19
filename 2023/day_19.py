from collections import deque

data = open(0).read().strip().split("\n\n")
ws = data[0].split("\n")
parts = data[1].split("\n")

workflows = {}

for w in ws:
    name, stuff = w.split("{")
    workflows[name] = stuff[:-1]

def solve(x, m, a, s):
    curr = "in"
    while True:
        workflow = workflows[curr]
        for op in workflow.split(","):
            next = op
            to_next = True
            if ":" in op:
                req, next = op.split(":")
                to_next = eval(req) # function arguments are used here
            if to_next:
                if next == "R":
                    return False
                elif next == "A":
                    return True
                else:
                    curr = next
                    break


p1 = 0
for part in parts:
    ratings = part.strip("\{\}").split(",")
    x = int(ratings[0][2:])
    m = int(ratings[1][2:])
    a = int(ratings[2][2:])
    s = int(ratings[3][2:])
    if solve(x, m, a, s):
        p1 += x + m + a + s

# this could have been formatted nicer, but I can't be bothered to change it
def range_stuff(thing, var, n):
    start, end = var
    if thing[0] == ">":
        if len(thing) == 1:
            start = max(n + 1, start)
        # create a range >=
        else:
            start = max(n, start)
    elif thing[0] == "<":
        if len(thing) == 1:
            end = min(n - 1, end)
        # create a range <=
        else:
            end = min(n, end)
    return (start, end)

p2 = 0
q = deque()
q.append(("in", (1, 4000), (1, 4000), (1, 4000), (1, 4000)))
while q:
    curr, x, m, a, s = q.pop()
    if x[1] < x[0] or m[1] < m[0] or a[1] < a[0] or s[1] < s[0] or curr == "R":
        continue
    elif curr == "A":
        p2 += (x[1] - x[0] + 1) * (m[1] - m[0] + 1) * (a[1] - a[0] + 1) * (s[1] - s[0] + 1)
        continue
    workflow = workflows[curr]
    for op in workflow.split(","):
        next = op
        if ":" in op:
            req, next = op.split(":")
            v = req[0]
            n = int(req[2:])
            thing = req[1]
            # naming is hard
            other_thing = "<<" if thing == ">" else ">>"
            if v == "x":
                q.append((next, range_stuff(thing, x, n), m, a, s))
                x = range_stuff(other_thing, x, n)
            elif v == "m":
                q.append((next, x, range_stuff(thing, m, n), a, s))
                m = range_stuff(other_thing, m, n)
            elif v == "a":
                q.append((next, x, m, range_stuff(thing, a, n), s))
                a = range_stuff(other_thing, a, n)
            elif v == "s":
                q.append((next, x, m, a, range_stuff(thing, s, n)))
                s = range_stuff(other_thing, s, n)
        else:
            q.append((next, x, m, a, s))
            break

print("p1 =", p1)
print("p2 =", p2)
