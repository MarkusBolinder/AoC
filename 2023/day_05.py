data = open(0).read().strip()
categories = data.split("\n\n")

# every entry is (destination range start, source range start, range length)
maps = [[] for _ in range(7)]
seeds = list(map(int, categories[0].split(": ")[1].split()))
seed_ranges = [x for x in seeds]

def create_list(category, new_list):
    for x in category.split("\n")[1:]:
        new_list.append(tuple(map(int, x.split())))


for i in range(len(maps)):
    create_list(categories[i + 1], maps[i])

for m in maps:
    for i in range(len(seeds)):
        seed = seeds[i]
        for dest_start, src_start, length in m:
            if src_start <= seed < src_start + length:
                seeds[i] = dest_start + seed - src_start
                # a seed can only change once per map
                break
print("p1 =", min(seeds))

ranges = list(zip(seed_ranges[::2], seed_ranges[1::2]))
seeds = []
for start, length in ranges:
    range = [(start, start + length)]
    for m in maps:
        changes = []
        for dest_start, src_start, map_length in m:
            new_range = []
            src_end = src_start + map_length
            while range:
                start, end = range.pop()
                start_range = (start, min(src_start, end))
                middle_range = (max(src_start, start), min(end, src_end))
                end_range = (max(start, src_end), end)
                if middle_range[0] < middle_range[1]:
                    changes.append((middle_range[0] - src_start + dest_start, middle_range[1] - src_start + dest_start))
                if start_range[0] < start_range[1]:
                    new_range.append(start_range)
                if end_range[0] < end_range[1]:
                    new_range.append(end_range)
            range = new_range
        range += changes
    seeds.append(min(range))
print("p2 =", min(seeds)[0])