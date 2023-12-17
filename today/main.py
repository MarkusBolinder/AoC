from collections import deque, defaultdict, Counter
import heapq

data = open(0).read().strip()
lines = data.split("\n")

grid = [[int(x) for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

