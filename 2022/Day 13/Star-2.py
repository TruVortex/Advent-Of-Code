input = open('input', 'r').read().split()


def compare(a, b):
    if isinstance(a, int):
        if isinstance(b, int):
            return b - a
        else:
            return compare([a], b)
    elif isinstance(b, int):
        return compare(a, [b])
    for x, y in zip(a, b):
        if compare(x, y):
            return compare(x, y)
    return len(b) - len(a)


idx_1, idx_2 = 1, 2
for line in input:
    if compare(eval(line), [[2]]) > 0:
        idx_1 += 1
    if compare(eval(line), [[6]]) > 0:
        idx_2 += 1
print(idx_1 * idx_2)
