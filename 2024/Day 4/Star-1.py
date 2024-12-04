grid, directions, cnt = open('input', 'r').read().split(), ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)), 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'X':
            for dx, dy in directions:
                if 0 <= i + 3 * dx < len(grid[0]) and 0 <= j + 3 * dy < len(grid):
                    if grid[i + dx][j + dy] == 'M' and grid[i + 2 * dx][j + 2 * dy] == 'A' and grid[i + 3 * dx][j + 3 * dy] == 'S':
                        cnt += 1
print(cnt)
