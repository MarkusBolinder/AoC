data = open(0).read().strip()
lines = data.split("\n")

id = 0
block = True
files = []
free = []
t = []
index = 0

for x in data:
    if block:
        for _ in range(int(x)):
            files.append((index, id))
            index += 1
            t.append(id)
        id += 1
        block = False
    else:
        free.append((index, int(x)))
        index += int(x)
        t.extend([None] * int(x))
        block = True

for file_index, file_id in reversed(files):
    for i, (free_index, free_size) in enumerate(free):
        if free_index < file_index and free_size > 0:
            t[file_index] = None
            t[free_index] = file_id
            free[i] = (free_index + 1, free_size - 1)
            break

p1 = 0
for i, x in enumerate(t):
    if x != None:
        p1 += i * x

# part 2
id = 0
block = True
files = []
free = []
t = []
index = 0

for x in data:
    x = int(x)
    if block:
        files.append((index, id, x))
        index += x
        t.extend([id] * x)
        id += 1
        block = False
    else:
        free.append((index, x))
        index += x
        t.extend([None] * x)
        block = True

for file_index, file_id, blocks in reversed(files):
    for i, (free_index, free_size) in enumerate(free):
        if free_index < file_index and free_size >= blocks:
            for j in range(blocks):
                t[file_index + j] = None
                t[free_index + j] = file_id
            free[i] = (free_index + blocks, free_size - blocks)
            break

p2 = 0
for i, x in enumerate(t):
    if x != None:
        p2 += i * x

print("p1 =", p1)
print("p2 =", p2)
