from collections import defaultdict

data = open(0).read().strip()
lines = data.split("\n")

score = 0

for line in lines:
    card = line.split(": ")
    numbers = card[1].split("|")
    winning = list(map(int, numbers[0].strip().split()))
    mine = list(map(int, numbers[1].strip().split()))
    matches = 0
    for n in mine:
        if n in winning:
            matches += 1
    if matches > 0:
        score += 2 ** (matches - 1)
print("p1 =", score)

# counts keeps track of how many times every game has occurred
counts = defaultdict(int)
games = [[int(x.split(": ")[0].split()[1]), x.split(": ")[1]] for x in lines]
for game in games:
    id = game[0]
    counts[id - 1] += 1
    numbers = game[1].split("|")
    winning = list(map(int, numbers[0].strip().split()))
    mine = list(map(int, numbers[1].strip().split()))
    matches = 0
    for n in mine:
        if n in winning:
            matches += 1
    # the next (matches) games are counted as many times as the current game
    for i in range(matches):
        counts[id + i] += counts[id - 1]
print("p2 =", sum(counts.values()))