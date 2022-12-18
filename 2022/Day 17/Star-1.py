moves = open('input', 'r').read().strip()
top, cnt = 0, 0
rocks = {(x, 0) for x in range(7)}
for i in range(2022):
    rock: tuple
    if i % 5 == 0:
        rock = ((2, top + 4), (3, top + 4), (4, top + 4), (5, top + 4))
    elif i % 5 == 1:
        rock = ((3, top + 4), (2, top + 5), (3, top + 5), (4, top + 5), (3, top + 6))
    elif i % 5 == 2:
        rock = ((2, top + 4), (3, top + 4), (4, top + 4), (4, top + 5), (4, top + 6))
    elif i % 5 == 3:
        rock = ((2, top + 4), (2, top + 5), (2, top + 6), (2, top + 7))
    else:
        rock = ((2, top + 4), (3, top + 4), (2, top + 5), (3, top + 5))
    while True:
        change_x = -1 if moves[cnt % len(moves)] == '<' else 1
        cnt += 1
        if all(((part[0] + change_x, part[1]) not in rocks and 0 <= part[0] + change_x <= 6) for part in rock):
            rock = tuple((part[0] + change_x, part[1]) for part in rock)
        if all((part[0], part[1] - 1) not in rocks for part in rock):
            rock = tuple((part[0], part[1] - 1) for part in rock)
        else:
            break
    top = max(top, rock[-1][1])
    rocks.update(rock)
print(top)
