schematic = ['.' + line + '.' for line in open('input', 'r').read().splitlines()]
schematic = ['.' * len(schematic[0])] + schematic + ['.' * len(schematic[0])]
summate = 0
for y in range(1, len(schematic) - 1):
    cur = 0
    part = False
    for x in range(1, len(schematic[0])):
        if schematic[y][x].isdigit():
            cur *= 10
            cur += int(schematic[y][x])
        else:
            if part:
                summate += cur
            cur = 0
            part = False
        part |= cur and ((not schematic[y][x - 1].isdigit() and schematic[y][x - 1] != '.') or (not schematic[y][x + 1].isdigit() and schematic[y][x + 1] != '.') or (not schematic[y - 1][x].isdigit() and schematic[y - 1][x] != '.') or (not schematic[y + 1][x].isdigit() and schematic[y + 1][x] != '.') or (not schematic[y - 1][x - 1].isdigit() and schematic[y - 1][x - 1] != '.') or (not schematic[y + 1][x - 1].isdigit() and schematic[y + 1][x - 1] != '.') or (not schematic[y - 1][x + 1].isdigit() and schematic[y - 1][x + 1] != '.') or (not schematic[y + 1][x + 1].isdigit() and schematic[y + 1][x + 1] != '.'))
print(summate)
