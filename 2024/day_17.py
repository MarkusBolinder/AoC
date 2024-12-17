from z3 import Solver, BitVec, sat

data = open(0).read().strip()

registers, program = data.split("\n\n")
registers = [int(register.split(": ")[1]) for register in registers.split("\n")]
program = list(map(int, program.split(": ")[1].split(",")))
n = len(program)

def run(registers, program):
    A, B, C = registers

    ip = 0
    output = []
    def get_combo(op):
        if op in range(4):
            return op
        else:
            return [A, B, C][op - 4]

    while ip < n:
        opcode = program[ip]
        if ip + 1 < n:
            operand = program[ip + 1]
        else:
            break

        # adv (0): A / combo() => A
        # bxl (1): B ^ lit() => B
        # bst (2): combo() % 8 => B
        # jnz (3): if A != 0 { jmp literal() }
        # bxc (4): B ^ C -> B (ignore operand)
        # out (5): output combo()
        # bdv (6): A / combo() => B
        # cdv (7): A / combo() => C

        if opcode == 0:
            combo = 2 ** get_combo(operand)
            if combo != 0:
                A = A // combo
            else:
                A = 0
            ip += 2
        elif opcode == 1:
            B ^= operand
            ip += 2
        elif opcode == 2:
            B = get_combo(operand) % 8
            ip += 2
        elif opcode == 3:
            if A != 0:
                ip = operand
            else:
                ip += 2
        elif opcode == 4:
            B ^= C
            ip += 2
        elif opcode == 5:
            output.append(get_combo(operand) % 8)
            ip += 2
        elif opcode == 6:
            combo = 2 ** get_combo(operand)
            if combo != 0:
                B = A // combo
            else:
                B = 0
            ip += 2
        elif opcode == 7:
            combo = 2 ** get_combo(operand)
            if combo != 0:
                C = A // combo
            else:
                C = 0
            ip += 2

    return ",".join(map(str, output))

p1 = run(registers, program)

solver = Solver()
A = BitVec("var", 3 * n + 1)
# it is just bit manipulations, but this took forever to figure out
for i in range(n):
    B = ((A >> (3 * i)) & 7) ^ 2
    C = A >> (3 * i + B)
    B ^= 7
    solver.add((B ^ C) & 7 == program[i])
    
while solver.check() == sat:
    p2 = solver.model()[A].as_long()
    solver.add(A < p2)

print("p1 =", p1)
print("p2 =", p2)
