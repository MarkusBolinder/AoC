from collections import deque, defaultdict
from math import gcd

data = open(0).read().strip()
lines = data.split("\n")

modules_to = {}
modules_from = defaultdict(list)
module_types = {}
conjunctions = defaultdict(dict)

for line in lines:
    module, dest = line.split(" -> ")
    dest = dest.split(", ")
    modules_to[module] = dest
    module_types[module[1:]] = module[0]

# modify the lists to have the correct type specifier
for module, to in modules_to.items():
    modules_to[module] = [m if m not in module_types else module_types[m] + m for m in to]

# False = low, True = high
for module, to in modules_to.items():
    for mod in to:
        if mod[0] == "&":
            conjunctions[mod][module] = False
        modules_from[mod].append(module)

# reused from day 8
def lcm(x):
    lcm = 1
    for xx in x:
        lcm = (xx * lcm) // gcd(xx, lcm)
    return lcm

# solving
high = set()
low_pulses = 0
high_pulses = 0
q = deque()
modules_that_send_to_the_module_that_sends_to_rx = modules_from[modules_from["rx"][0]]
last_encounter = {}
number_of_important_encounters = defaultdict(int)
cycles = []
done = False
p1 = 0
p2 = 0
for t in range(1_000_000_000):
    q.append(("broadcaster", "button", False))
    while q:
        module, origin, on = q.popleft()

        # part 2 logic:
        # need to find how long the cycles for a module sending to rx is essentially
        # we then want to find when these modules receive a low pulse, and finally calculate lcm
        # the modules that are relevant are the ones that send to the ones that send to rx
        # rx receives signals from &cs
        # cs receives singals from &kh, &lz, &tg, &hn
        # this means that we should count the number of occurences of &kh, &lz, &tg, &hn
        # and whenever they have appeared twice, we add the cycle length to a list used to calculate lcm
        # assuming the problem works out nicely so that these assumptions hold
        if not on:
            if module in modules_that_send_to_the_module_that_sends_to_rx and number_of_important_encounters[module] == 2 and module in last_encounter:
                cycles.append(t - last_encounter[module])
            last_encounter[module] = t
            number_of_important_encounters[module] += 1
            if len(cycles) == len(modules_that_send_to_the_module_that_sends_to_rx):
                p2 = lcm(cycles)
                done = True
                break
        if on:
            high_pulses += 1
        else:
            low_pulses += 1
        if module in modules_to:
            if module == "broadcaster":
                for to_module in modules_to[module]:
                    q.append((to_module, module, on))
            elif module[0] == "%":
                # flip-flops ignore high pulses
                if not on:
                    if module in high:
                        on = False
                        high.remove(module)
                    else:
                        on = True
                        high.add(module)
                    for to_module in modules_to[module]:
                        q.append((to_module, module, on))
            elif module[0] == "&":
                conjunctions[module][origin] = on
                # the conjunction sends a low pulse if all pulses to it are high, otherwise it sends a low pulse
                on = False if all(pulse for pulse in conjunctions[module].values()) else True
                for to_module in modules_to[module]:
                    q.append((to_module, module, on))
    if t == 1000 - 1:
        p1 = low_pulses * high_pulses
    if done:
        break

print("p1 =", p1)
print("p2 =", p2)
