from collections import deque

data = open(0).read().strip()
input, gates = data.split("\n\n")

wires = {}
ops = deque()

for wire in input.split("\n"):
    wire, bit = wire.split(": ")
    wires[wire] = int(bit)

for gate in gates.split("\n"):
    in1, op, in2, _, out = gate.split(" ")
    ops.append((op, in1, in2, out))

wrong = set()
for op, in1, in2, out in ops:
    if (
        (out.startswith("z") and op != "XOR") or
        (op == "XOR" and all(w[0] not in "xyz" for w in (out, in1, in2)))
        ):
        wrong.add(out)
    if (op == "AND" and "x00" not in [in1, in2]) or op == "XOR":
        for nop, nin1, nin2, nout in ops:
            if (
                (out == nin1 or out == nin2) and
                ((op == "AND" and nop != "OR") or (op, nop) == ("XOR", "OR"))
                ):
                wrong.add(out)
wrong.discard("z45")

while ops:
    op, in1, in2, out = ops.popleft()
    if in1 in wires and in2 in wires:
        w1, w2 = wires[in1], wires[in2]
        wires[out] = {"AND": w1 & w2, "OR": w1 | w2, "XOR": w1 ^ w2}[op]
    else:
        ops.append((op, in1, in2, out))

bits = "".join([str(bit) for wire, bit in sorted(wires.items()) if wire.startswith("z")])
p1 = int(bits[::-1], 2)
p2 = ",".join(sorted(wrong))
print("p1 =", p1)
print("p2 =", p2)
