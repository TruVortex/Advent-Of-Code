x = y = direction = 0
seen, delta = {(0, 0)}, ((0, 1), (1, 0), (0, -1), (-1, 0))
for instruction in open('input', 'r').read().split(', '):
    if instruction[0] == 'R':
        direction += 1
    else:
        direction -= 1
    direction %= 4
    for _ in range(int(instruction[1:])):
        x += delta[direction][0]
        y += delta[direction][1]
        if (x, y) in seen:
            print(abs(x) + abs(y))
            exit(0)
        seen.add((x, y))
