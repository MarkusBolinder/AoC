from collections import deque, defaultdict, Counter
import heapq
from math import gcd
from copy import deepcopy

data = open(0).read().strip()
lines = data.split("\n")

grid = [[x for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

for line in lines:
    pass

