import math

instructions, temp = open('input', 'r').read().split('\n\n')
instructions = list(map(int, instructions.replace('L', '0').replace('R', '1')))
new, cur, end = temp + '\n', [], set()
for i in range(len(temp) - 16, -1, -17):
    new = new.replace(temp[i:i + 3], str(i // 17))
    if temp[i + 2] == 'A':
        cur.append(i // 17)
    elif temp[i + 2] == 'Z':
        end.add(i // 17)
nodes = []
while '\n' in new:
    nodes.append(eval(new[new.find('('):new.find('\n')]))
    new = new[new.find('\n') + 1:]
cycles = []
for i, pos in enumerate(cur):
    cnt, steps = 1, 0
    while not steps or pos not in end:
        pos = nodes[pos][instructions[steps % len(instructions)]]
        steps += 1
    cycles.append(steps)
print(math.lcm(*cycles))
