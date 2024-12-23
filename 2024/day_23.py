import networkx as nx

data = open(0).read().strip()
lines = data.split("\n")

edges = []
for line in lines:
    edges.append(line.split("-"))

graph = nx.Graph(edges)
cliques = list(nx.enumerate_all_cliques(graph))

p1 = 0
for clique in cliques:
    if len(clique) == 3 and any([node.startswith("t") for node in clique]):
        p1 += 1

cliques = [",".join(sorted(clique)) for clique in cliques]
p2 = max(cliques, key=lambda clique: len(clique))

print("p1 =", p1)
print("p2 =", p2)
