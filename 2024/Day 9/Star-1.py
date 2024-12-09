line, available, compact, total = list(map(int, list(open('input', 'r').readline().strip()))), [], [], 0
for i, blocks in enumerate(line):
    if i % 2:
        compact += ['.'] * blocks
    else:
        compact += ['#'] * blocks
        available += [i // 2] * blocks
for i in range(len(available)):
    if compact[i] == '#':
        total += available.pop(0) * i
    else:
        total += available.pop() * i
print(total)
