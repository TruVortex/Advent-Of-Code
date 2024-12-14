import re

machines, total = open('input', 'r').read().split('\n\n'), 0
for machine in machines:
    button1, button2, prize = machine.split('\n')
    button1, button2, prize, cost = list(map(int, re.findall(r'(?<=\+)\d+', button1))), list(map(int, re.findall(r'(?<=\+)\d+', button2))), list(map(int, re.findall(r'(?<==)\d+', prize))), 1e9
    for i in range(0, prize[0] // button1[0] + 1):
        if (prize[0] - i * button1[0]) % button2[0] == 0 and (prize[0] - i * button1[0]) / button2[0] == (prize[1] - i * button1[1]) / button2[1]:
            cost = min(cost, 3 * i + (prize[0] - i * button1[0]) // button2[0])
    if cost != 1e9:
        total += cost
print(total)
