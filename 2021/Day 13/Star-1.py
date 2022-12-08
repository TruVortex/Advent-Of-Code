grid, commands = open('input', 'r').read().split('\n\n')
dots = set()
for dot in grid.split():
    dots.add(tuple(map(int, dot.split(','))))
line = commands.splitlines()[0][11:].split('=')
if line[0] == 'x':
    dots = {(x if x < int(line[1]) else int(line[1]) * 2 - x, y) for x, y in dots}
else:
    dots = {(x, y if y < int(line[1]) else int(line[1]) * 2 - y) for x, y in dots}
print(len(dots))
