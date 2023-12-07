from functools import cmp_to_key
from collections import Counter

data = open(0).read().strip()
lines = data.split("\n")

hands = []

ranks = {
    "A" : 12,
    "K" : 11,
    "Q" : 10,
    "J" : 9,
    "T" : 8,
    "9" : 7,
    "8" : 6,
    "7" : 5,
    "6" : 4,
    "5" : 3,
    "4" : 2,
    "3" : 1,
    "2" : 0
    }

for line in lines:
    hand = line.split()
    hands.append((hand[0], int(hand[1])))

# this is terrible
def cmp(h1, h2):
    x = h1[0]
    xx = [x.count(c) for c in ranks.keys()]
    y = h2[0]
    yy = [y.count(c) for c in ranks.keys()]
    if 5 in xx and 5 in yy:
        if ranks[x[0]] > ranks[y[0]]:
            return 1
        elif ranks[x[0]] < ranks[y[0]]:
            return -1
        else:
            return 0
    elif 5 in xx:
        return 1
    elif 5 in yy:
        return -1
    if 4 in xx and 4 in yy:
        for i in range(5):
            if ranks[x[i]] > ranks[y[i]]:
                return 1
            elif ranks[x[i]] < ranks[y[i]]:
                return -1
    elif 4 in xx:
        return 1
    elif 4 in yy:
        return -1
    if 3 in xx and 2 in xx and 3 in yy and 2 in yy:
        for i in range(5):
            if ranks[x[i]] > ranks[y[i]]:
                return 1
            elif ranks[x[i]] < ranks[y[i]]:
                return -1
    elif 3 in xx and 2 in xx:
        return 1
    elif 3 in yy and 2 in yy:
        return -1
    if 3 in xx and 3 in yy:
        for i in range(5):
            if ranks[x[i]] > ranks[y[i]]:
                return 1
            elif ranks[x[i]] < ranks[y[i]]:
                return -1
    elif 3 in xx:
        return 1
    elif 3 in yy:
        return -1
    if xx.count(2) == 2 and yy.count(2) == 2:
        for i in range(5):
            if ranks[x[i]] > ranks[y[i]]:
                return 1
            elif ranks[x[i]] < ranks[y[i]]:
                return -1
    elif xx.count(2) == 2:
        return 1
    elif yy.count(2) == 2:
        return -1
    if 2 in xx and 2 in yy:
        for i in range(5):
            if ranks[x[i]] > ranks[y[i]]:
                return 1
            elif ranks[x[i]] < ranks[y[i]]:
                return -1
    elif 2 in xx:
        return 1
    elif 2 in yy:
        return -1
    for i in range(5):
        if ranks[x[i]] > ranks[y[i]]:
            return 1
        elif ranks[x[i]] < ranks[y[i]]:
            return -1

result_p1 = sorted(hands, key=cmp_to_key(cmp))
p1 = 0
for i, (_, rank) in enumerate(result_p1):
    p1 += rank * (i + 1)
print(p1)



replacements = {
    "A" : chr(ord("9")+5),
    "K" : chr(ord("9")+4),
    "Q" : chr(ord("9")+3),
    "J" : chr(ord("2")-1),
    "T" : chr(ord("9")+1)
    }

def create_hand(hand):
    for k, v in replacements.items():
        hand = hand.replace(k, v)
    return hand

def cmp2(hand):
    x = create_hand(hand[0])
    xx = Counter(x)
    best_rank = x[0]
    jokers = x.count("1")
    if jokers:
        for rank in xx.keys():
            if rank != "1" and (xx[rank] > xx[best_rank] or best_rank == "1"):
                best_rank = rank
        if best_rank != "1":
            xx[best_rank] += jokers
            xx.pop("1")
    xx = sorted(list(xx.values()))
    if xx == [5]:
        return (6, x)
    elif xx == [1, 4]:
        return (5, x)
    elif xx == [2, 3]:
        return (4, x)
    elif xx == [1, 1, 3]:
        return (3, x)
    elif xx == [1, 2, 2]:
        return (2, x)
    elif xx == [1, 1, 1, 2]:
        return (1, x)
    elif xx == [1, 1, 1, 1, 1]:
        return (0, x)
    else:
        print("error")
        exit(1)
    
result_p2 = sorted(hands, key=lambda x: cmp2(x))
p2 = 0
for i, (_, rank) in enumerate(result_p2):
    p2 += rank * (i + 1)
print(p2)