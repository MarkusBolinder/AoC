from collections import deque, defaultdict, Counter
from math import gcd
from copy import deepcopy
import sys
from z3 import *

data = open(0).read().strip()
lines = data.split("\n")

sys.setrecursionlimit(10 ** 5)

grid = [[x for x in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

for line in lines:
    pass

