schematic = ['.' + line + '.' for line in open('input', 'r').read().splitlines()]
schematic = ['.' * len(schematic[0])] + schematic + ['.' * len(schematic[0])]


def get_num(yy, xx):
    global schematic
    if schematic[yy][xx] == '.':
        return -1, -1
    while schematic[yy][xx].isdigit():
        xx -= 1
    xx += 1
    start = xx
    while schematic[yy][xx].isdigit():
        xx += 1
    return int(schematic[yy][start:xx]), start


summate = 0
for y in range(1, len(schematic) - 1):
    cur = 0
    part = False
    for x in range(1, len(schematic[0]) - 1):
        if schematic[y][x] == '*':
            distinct = {get_num(y, x - 1), get_num(y, x + 1), get_num(y - 1, x), get_num(y + 1, x), get_num(y - 1, x - 1), get_num(y + 1, x - 1), get_num(y - 1, x + 1), get_num(y + 1, x + 1)}
            if len(distinct) == 3:
                cur = -1
                for part in distinct:
                    cur *= part[0]
                summate += cur
print(summate)
