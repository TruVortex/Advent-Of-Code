groups = list(map(str.splitlines, open('input', 'r').read().split('\n\n')))


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


cnt = 0
for idx, group in enumerate(groups, 1):
    if compare(eval(group[0]), eval(group[1])) > 0:
        cnt += idx
print(cnt)
