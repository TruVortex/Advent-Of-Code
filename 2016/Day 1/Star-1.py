x = y = direction = 0
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
for instruction in open('input', 'r').read().split(', '):
    if instruction[0] == 'R':
        direction += 1
    else:
        direction -= 1
    direction %= 4
    x += delta[direction][0] * int(instruction[1:])
    y += delta[direction][1] * int(instruction[1:])
print(abs(x) + abs(y))
