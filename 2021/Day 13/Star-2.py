grid, commands = open('input', 'r').read().split('\n\n')
dots = set()
for dot in grid.split():
    dots.add(tuple(map(int, dot.split(','))))
for line in commands.splitlines():
    line = line[11:].split('=')
    if line[0] == 'x':
        dots = {(x if x < int(line[1]) else int(line[1]) * 2 - x, y) for x, y in dots}
    else:
        dots = {(x, y if y < int(line[1]) else int(line[1]) * 2 - y) for x, y in dots}
grid = [[' ' for i in range(40)] for j in range(6)]
for x, y in dots:
    grid[y][x] = '#'
for i in range(6):
    print(grid[i])
