from collections import defaultdict

data = open(0).read().strip()
lines = data.split("\n")

servers = dict()
for line in lines:
    line = line.split(":")
    server = line[0].strip()
    outputs = line[1].strip().split()
    servers[server] = outputs

seen = defaultdict(int)
def solve(state, part2):
    if state in seen:
        return seen[state]
    if part2:
        server, fft, dac = state
    else:
        server = state
    if server == "out":
        if not part2 or fft and dac:
            seen[state] = 1
        else:
            seen[state] = 0
    else:
        for out in servers[server]:
            if part2:
                new_fft = fft | (out == "fft")
                new_dac = dac | (out == "dac")
                new_state = (out, new_fft, new_dac)
            else:
                new_state = out
            seen[state] += solve(new_state, part2)
    return seen[state]

p1 = solve("you", False)
seen = defaultdict(int)
p2 = solve(("svr", False, False), True)

print("p1 =", p1)
print("p2 =", p2)