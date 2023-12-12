data = open(0).read().strip()
lines = data.split("\n")
springs = []
damage_list = []

for line in lines:
    stuff = line.split()
    springs.append(stuff[0])
    damage_list.append(eval("[" + stuff[1] + "]"))


# cache results for a given line
seen = {}

# need to keep track of index in current spring and the current group in damages
def solve(spring, damages, current_group, length_of_group, i):
    k = (current_group, length_of_group, i)
    if k in seen:
        return seen[k]
    groups = len(damages)
    if i == len(spring):
        res = 1 if (current_group == groups - 1 and damages[current_group] == length_of_group) or (length_of_group == 0 and current_group == groups) else 0
        return res
    combinations = 0
    c = spring[i]
    if c == "?" or c == ".":
        if length_of_group == 0:
            combinations += solve(spring, damages, current_group, 0, i + 1)
        elif current_group < groups and damages[current_group] == length_of_group:
            combinations += solve(spring, damages, current_group + 1, 0, i + 1)
    if c == "?" or c == "#":
        combinations += solve(spring, damages, current_group, length_of_group + 1, i + 1)
    seen[k] = combinations
    return combinations
        

p1 = 0
for spring, damages in zip(springs, damage_list):
    seen.clear()
    p1 += solve(spring, damages, 0, 0, 0)

for i in range(len(springs)):
    springs[i] += "?"
    springs[i] *= 5
    springs[i] = springs[i][:-1]
    damage_list[i] *= 5

p2 = 0
for spring, damages in zip(springs, damage_list):
    seen.clear()
    p2 += solve(spring, damages, 0, 0, 0)

print("p1 =", p1)
print("p2 =", p2)
