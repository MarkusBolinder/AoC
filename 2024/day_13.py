from z3 import Solver, IntVector, sat

data = open(0).read().strip()
machine_data = data.split("\n\n")

machines = []

for machine in machine_data:
    info = machine.split("\n")
    A = info[0].split(": ")[1].split(", ")
    A = (int(A[0][2:]), int(A[1][2:]))
    B = info[1].split(": ")[1].split(", ")
    B = (int(B[0][2:]), int(B[1][2:]))
    prize = info[2].split(": ")[1].split(", ")
    prize = (int(prize[0][2:]), int(prize[1][2:]))
    machines.append((A, B, prize))

def solve(machines):
    t = 0
    for (ax, ay), (bx, by), (px, py) in machines:
        s = Solver()
        P = IntVector("P", 2)
        cost = P[0] * 3 + P[1]

        # constraints for button presses
        s.add(P[0] >= 0)
        s.add(P[1] >= 0)
        s.add(P[0] * ax + P[1] * bx == px)
        s.add(P[0] * ay + P[1] * by == py)

        low = None
        while s.check() == sat:
            model = s.model()
            curr = model.eval(cost).as_long()
            if low is None or curr < low:
                low = curr
            # block current or worse solutions
            s.add(cost < curr)
        if low is not None:
            t += low
    return t

p1 = solve(machines)
for i, (A, B, (px, py)) in enumerate(machines):
    machines[i] = (A, B, (px + 10 ** 13, py + 10 ** 13))
p2 = solve(machines)

print("p1 =", p1)
print("p2 =", p2)
