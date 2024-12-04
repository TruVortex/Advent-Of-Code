grid, cnt = open('input', 'r').read().split(), 0
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        if grid[i][j] == 'A' and {grid[i - 1][j - 1], grid[i + 1][j + 1]} == {grid[i - 1][j + 1], grid[i + 1][j - 1]} == {'M', 'S'}:
            cnt += 1
print(cnt)
