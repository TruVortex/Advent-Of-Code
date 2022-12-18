moves = open('input', 'r').read().strip()
ans = top = cnt = period = 0
fall, rocks, seen, flag, = 1e9, {(x, 0) for x in range(7)}, {}, False
while fall:
    rock: tuple
    if period % 5 == 0:
        rock = ((2, top + 4), (3, top + 4), (4, top + 4), (5, top + 4))
    elif period % 5 == 1:
        rock = ((3, top + 4), (2, top + 5), (3, top + 5), (4, top + 5), (3, top + 6))
    elif period % 5 == 2:
        rock = ((2, top + 4), (3, top + 4), (4, top + 4), (4, top + 5), (4, top + 6))
    elif period % 5 == 3:
        rock = ((2, top + 4), (2, top + 5), (2, top + 6), (2, top + 7))
    else:
        rock = ((2, top + 4), (3, top + 4), (2, top + 5), (3, top + 5))
    while True:
        change_x = -1 if moves[cnt] == '<' else 1
        cnt += 1
        cnt %= len(moves)
        if all(((part[0] + change_x, part[1]) not in rocks and 0 <= part[0] + change_x <= 6) for part in rock):
            rock = tuple((part[0] + change_x, part[1]) for part in rock)
        if all((part[0], part[1] - 1) not in rocks for part in rock):
            rock = tuple((part[0], part[1] - 1) for part in rock)
        else:
            break
    top = max(top, rock[-1][1])
    rocks.update(rock)
    fall -= 1
    period += 1
    if (period % 5, rock[0][0], cnt) in seen and not flag:
        before = seen[(period % 5, rock[0][0], cnt)]
        fall = (1e12 - period) % (period - before[1])
        ans = ((1e12 - period) // (period - before[1])) * (top - before[0])
        flag = True
    seen[(period % 5, rock[0][0], cnt)] = (top, period)
print(int(ans) + top)
