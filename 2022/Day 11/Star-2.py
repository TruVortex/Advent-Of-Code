input = open('input', 'r')
mod, monkey_groups, monkeys = 1, input.read().split('\n\n'), []
for group in monkey_groups:
    lines = group.splitlines()
    monkeys.append([list(map(int, lines[1][18:].split(','))), eval(f'lambda old: {lines[2][19:]}'), *map(int, [lines[i].split()[-1] for i in range(3, 6)])])
    mod *= monkeys[-1][2]
freq = [0] * len(monkeys)
for i in range(10000):
    for idx, monkey in enumerate(monkeys):
        freq[idx] += len(monkey[0])
        for item in monkey[0]:
            new = monkey[1](item) % mod
            if new % monkey[2]:
                monkeys[monkey[4]][0].append(new)
            else:
                monkeys[monkey[3]][0].append(new)
        monkey[0] = []
freq.sort()
print(freq[-1] * freq[-2])
