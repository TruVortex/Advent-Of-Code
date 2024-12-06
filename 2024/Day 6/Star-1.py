grid, x, y, direction, directions = [list(line) for line in open('input', 'r')], -1, -1, 0, ((0, -1), (1, 0), (0, 1), (-1, 0))
for i, line in enumerate(grid):
    if '^' in line:
        x = line.index('^')
        y = i
while 0 <= x < len(grid[0]) and 0 <= y < len(grid):
    if grid[y][x] == '#':
        x -= directions[direction][0]
        y -= directions[direction][1]
        direction = (direction + 1) % 4
    else:
        grid[y][x] = 'X'
        x += directions[direction][0]
        y += directions[direction][1]
print(sum(line.count('X') for line in grid))
