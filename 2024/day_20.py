from networkx import *

data = open(0).read().strip()
grid = [list(row) for row in data.split("\n")]
rows = len(grid)
cols = len(grid[0])

def solve(max_steps):
    start = None
    end = None
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "S":
                start = (x, y)
            elif grid[x][y] == "E":
                end = (x, y)

    def construct_graph(walls):
        graph = Graph()
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "#" and not walls:
                    continue
                for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and (walls or grid[nx][ny] in ".SE"):
                        graph.add_edge((x, y), (nx, ny))
        return graph

    graph = construct_graph(False)
    wall_graph = construct_graph(True)
    
    try:
        norm_time = shortest_path_length(graph, start, end)
    except NetworkXNoPath:
        return 0

    start_dist = single_source_dijkstra_path_length(graph, start)
    end_dist = single_source_dijkstra_path_length(graph, end)

    saved = []
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] not in ".SE" or (x, y) not in start_dist:
                continue
            d1 = start_dist[(x, y)]
            cheats = single_source_dijkstra_path_length(wall_graph, (x, y), cutoff=max_steps)
            for (cx, cy), cd in cheats.items():
                if grid[cx][cy] not in ".SE" or (cx, cy) not in start_dist:
                    continue
                d2 = end_dist[(cx, cy)]
                cheat_time = d1 + cd + d2
                saved_time = norm_time - cheat_time
                if saved_time >= 100:
                    saved.append(saved_time)

    return len(saved)

p1 = solve(2)
p2 = solve(20)

print("p1 =", p1)
print("p2 =", p2)
