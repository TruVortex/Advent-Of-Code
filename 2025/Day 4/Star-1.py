grid, dirs, cnt = ['.' + line.strip() + '.' for line in open('input', 'r')], ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)), 0
grid = ['.' * len(grid[0])] + grid + ['.' * len(grid[0])]
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        if grid[i][j] == '@' and sum(grid[i + dx][j + dy] == '@' for (dx, dy) in dirs) < 4:
            cnt += 1
print(cnt)
