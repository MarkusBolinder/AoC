from collections import defaultdict
import networkx as nx

data = open(0).read().strip()
lines = data.split("\n")

wires = set()
connections = defaultdict(list)

for line in lines:
    stuff = line.split(": ")
    more_stuff = stuff[1].split(" ")
    wires.add(stuff[0])
    for x in more_stuff:
        wires.add(x)

for line in lines:
    stuff = line.split(": ")
    left = stuff[0]
    right = stuff[1].split(" ")
    for wire in right:
        connections[left].append(wire)
        connections[wire].append(left)

# networkx op
graph = nx.DiGraph()

for k, v in connections.items():
    for vv in v:
        graph.add_edge(k, vv, capacity=1)
        graph.add_edge(vv, k, capacity=1)

start = lines[0].split(": ")[0]
for wire in connections.keys():
    if wire != start:
        cuts, (left, right) = nx.minimum_cut(graph, start, wire)
        if cuts == 3:
            break

p1 = len(left) * len(right)
print("p1 =", p1)
