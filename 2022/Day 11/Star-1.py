input = open('input', 'r')
monkey_groups, monkeys = input.read().split('\n\n'), []
for group in monkey_groups:
    lines = group.splitlines()
    monkeys.append([list(map(int, lines[1][18:].split(','))), eval(f'lambda old: {lines[2][19:]}'), *map(int, [lines[i].split()[-1] for i in range(3, 6)])])
freq = [0] * len(monkeys)
for i in range(20):
    for idx, monkey in enumerate(monkeys):
        freq[idx] += len(monkey[0])
        for item in monkey[0]:
            new = monkey[1](item) // 3
            if new % monkey[2]:
                monkeys[monkey[4]][0].append(new)
            else:
                monkeys[monkey[3]][0].append(new)
        monkey[0] = []
freq.sort()
print(freq[-1] * freq[-2])
