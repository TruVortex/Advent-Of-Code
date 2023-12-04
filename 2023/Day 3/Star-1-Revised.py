schematic = ['.' + line + '.' for line in open('input', 'r').read().splitlines()]
schematic = ['.' * len(schematic[0])] + schematic + ['.' * len(schematic[0])]


def get_num(yy, xx):
    global schematic
    if schematic[yy][xx] == '.':
        return 0, -1, -1
    while schematic[yy][xx].isdigit():
        xx -= 1
    xx += 1
    start = xx
    while schematic[yy][xx].isdigit():
        xx += 1
    return int(schematic[yy][start:xx]), yy, start


distinct = set()
for y in range(1, len(schematic) - 1):
    for x in range(1, len(schematic[0]) - 1):
        if not schematic[y][x].isdigit() and schematic[y][x] != '.':
            distinct.update([get_num(y, x - 1), get_num(y, x + 1), get_num(y - 1, x), get_num(y + 1, x), get_num(y - 1, x - 1), get_num(y + 1, x - 1), get_num(y - 1, x + 1), get_num(y + 1, x + 1)])
summate = 0
for part in distinct:
    summate += part[0]
print(summate)
