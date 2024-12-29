import z3
import random
from itertools import product, combinations

# Note: I solved part 2 manually at first, then I wanted to figure out how it could be done manually.
# The code for part 2 here is heavily based on discussions I found on the subreddit.

initial_wires, gate_definitions = open(0).read().strip().split("\n\n")

wire_values = {}
for wire, value in (line.split(": ") for line in initial_wires.split("\n")):
    wire_values[wire] = int(value)

gate_operations = {}
for operation, output in (line.split(" -> ") for line in gate_definitions.split("\n")):
    gate_operations[output] = tuple(operation.split())

output_wires = sorted([wire for wire in gate_operations if wire.startswith("z")], key=lambda x: int(x[1:]), reverse=True)

def simulate_gates(wire_values):
    num_output_wires = len(output_wires)
    count = 0

    while count < num_output_wires:
        for output_wire, (in1, op, in2) in gate_operations.items():
            if output_wire in wire_values:
                continue
            if in1 in wire_values and in2 in wire_values:
                x, y = wire_values[in1], wire_values[in2]
                wire_values[output_wire] = x & y if op == "AND" else x | y if op == "OR" else x ^ y
                if output_wire in output_wires:
                    count += 1

    result = "".join(str(wire_values[wire]) for wire in output_wires)
    return int(result, 2)

solver = z3.Solver()
vars = {key: z3.BitVec(key, 46) for key in list(wire_values) + list(gate_operations)}

for output_wire, (in1, op, in2) in gate_operations.items():
    out, in1, in2 = vars[output_wire], vars[in1], vars[in2]
    solver.add(out == (in1 & in2 if op == "AND" else in1 | in2 if op == "OR" else in1 ^ in2))

x_wires = [f"x{i:02}" for i in range(45)]
y_wires = [f"y{i:02}" for i in range(45)]

seen = {}
def generate_tests(bit_index):
    if bit_index in seen:
        random.shuffle(seen[bit_index])
        return seen[bit_index]

    max_difficulty = 6
    if bit_index < max_difficulty:
        tests = list(product(range(1 << bit_index), repeat=2))
    else:
        tests = [(random.randrange(1 << bit_index), random.randrange(1 << bit_index)) for _ in range(1 << (2 * max_difficulty))]

    seen[bit_index] = tests
    random.shuffle(tests)
    return tests

def build_adjacency_list():
    adj_list = {key: [in1, in2] for key, (in1, _, in2) in gate_operations.items()}
    adj_list.update({key: [] for key in wire_values})
    return adj_list

def has_cycle():
    adj_list = build_adjacency_list()
    visited, stack = set(), set()

    def dfs(node):
        if node in stack:
            return True
        if node in visited:
            return False

        visited.add(node)
        stack.add(node)
        if any(dfs(neighbor) for neighbor in adj_list.get(node, [])):
            return True
        stack.remove(node)
        return False

    return any(dfs(node) for node in adj_list)

def bfs(adj_list, *start_nodes):
    distances = dict.fromkeys(start_nodes, 0)
    q = list(start_nodes)
    pred = {node: node for node in start_nodes}
    for node in q:
        d= distances[node]
        for neighbor in adj_list.get(node, []):
            if neighbor not in distances:
                distances[neighbor] = d+ 1
                pred[neighbor] = node
                q.append(neighbor)
    return distances, q, pred

def correct_circuit(bit_index, swapped_wires):
    if bit_index == 46:
        print("p2 =", ",".join(sorted(swapped_wires)))
        exit()

    def get_wire_value(wire, n1, n2):
        if wire.startswith("x"):
            return (n1 >> int(wire[1:])) & 1
        if wire.startswith("y"):
            return (n2 >> int(wire[1:])) & 1
        in1, op, in2 = gate_operations[wire]
        x, y = get_wire_value(in1, n1, n2), get_wire_value(in2, n1, n2)
        return x & y if op == "AND" else x | y if op == "OR" else x ^ y

    def okay():
        return all(
            get_wire_value(f"z{bit:02}", n1, n2) == ((n1 + n2) >> bit) & 1
            for n1, n2 in generate_tests(bit_index) for bit in range(bit_index + 1)
        )
    
    print(bit_index, okay(), swapped_wires)

    if okay():
        correct_circuit(bit_index + 1, swapped_wires)
        return
    if len(swapped_wires) == 8:
        return
    
    adj_list = build_adjacency_list()
    internal_wires = set(bfs(adj_list, f"z{bit_index:02}")[1]) - set(wire_values) - swapped_wires
    external_wires = set(gate_operations) - swapped_wires
    candidates = list(product(internal_wires, external_wires)) + list(combinations(internal_wires, 2))
    random.shuffle(candidates)

    for wire1, wire2 in candidates:
        if wire1 == wire2:
            continue
        gate_operations[wire1], gate_operations[wire2] = gate_operations[wire2], gate_operations[wire1]
        swapped_wires.update([wire1, wire2])
        if not has_cycle() and okay():
            correct_circuit(bit_index, swapped_wires)
        swapped_wires.difference_update([wire1, wire2])
        gate_operations[wire1], gate_operations[wire2] = gate_operations[wire2], gate_operations[wire1]

p1 = simulate_gates(wire_values.copy())
print("p1 =", p1)
correct_circuit(0, set())
exit()
