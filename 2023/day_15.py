data = open(0).read().strip()
seqs = data.split(",")

def hash(x):
    value = 0
    for c in x:
        value = ((value + ord(c)) * 17) % 256
    return value


p1 = 0
for seq in seqs:
    p1 += hash(seq)

boxes = [[] for _ in range(256)]
for seq in seqs:
    if seq[-1] == "-":
        label = seq[:-1]
        h = hash(label)
        boxes[h] = [(lab, foc) for lab, foc in boxes[h] if lab != label]
    else:
        label = seq[:-2]
        focal = int(seq[-1])
        h = hash(label)
        if label not in [lab for lab, _ in boxes[h]]:
            boxes[h].append((label, focal))
        else:
            boxes[h] = [(lab, foc) if lab != label else (lab, focal) for lab, foc in boxes[h]]
p2 = 0
for i, box in enumerate(boxes):
    for j, (_, f) in enumerate(box):
        p2 += (i + 1) * (j + 1) * f

print("p1 =", p1)
print("p2 =", p2)
