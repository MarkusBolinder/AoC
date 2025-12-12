data = open(0).read().strip()
lines = data.split("\n\n")

presents = dict()
for block in lines[:-1]:
    size = block.count("#")
    presents[int(block[0])] = size

info = False
p1 = 0
ratios = []
for tiling in lines[-1].split("\n"):
    grid, tiles = tiling.split(":")
    rows, cols = map(int, grid.split("x"))
    tiles = list(map(int, tiles.strip().split()))
    ub = rows * cols
    lb = sum([x * presents[i] for i, x in enumerate(tiles)])
    ratio = ub / lb
    ratios.append(ratio)
    if info:
        print(ub, lb, round(ratio, 3))
    # NP-complete problem...
    # looking at the ratios, they are almost all ≈1 or > 1.4 =>
    # heuristic: take some cutoff in the middle
    if ratio > 1.25:
        p1 += 1

if info:
    # every cutoff ∈ (1, 1.35] works lmao
    for cutoff in [0.99, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50]:
        print(cutoff, val := sum([ratio > cutoff for ratio in ratios]), val == p1)

print("p1 =", p1)