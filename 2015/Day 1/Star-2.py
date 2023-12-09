floor = 0
for i, move in enumerate(open('input', 'r').readline()):
    floor += 1 - 2 * (move == ')')
    if floor < 0:
        print(i + 1)
        break
