grid, x, y, directions, cnt = [list(line) for line in open('input', 'r')], -1, -1, ((0, -1), (1, 0), (0, 1), (-1, 0)), 0
for i, line in enumerate(grid):
    if '^' in line:
        x = line.index('^')
        y = i
for line in grid:
    for i in range(len(line)):
        if line[i] == '.':
            line[i], seen, nx, ny, direction = '#', set(), x, y, 0
            while 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                if grid[ny][nx] == '#':
                    nx -= directions[direction][0]
                    ny -= directions[direction][1]
                    direction = (direction + 1) % 4
                else:
                    nx += directions[direction][0]
                    ny += directions[direction][1]
                if (nx, ny, direction) in seen:
                    cnt += 1
                    break
                seen.add((nx, ny, direction))
            line[i] = '.'
print(cnt)
