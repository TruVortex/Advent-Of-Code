input = open('input', 'r')
grid = ['9' * 100] + input.read().split() + ['9' * 100]
for i in range(len(grid)):
    grid[i] = '9' + grid[i] + '9'
ans = 0
for i in range(1, len(grid)):
    for j in range(1, len(grid[1])):
        if grid[i][j] < grid[i - 1][j] and grid[i][j] < grid[i + 1][j] and grid[i][j] < grid[i][j - 1] and grid[i][j] < grid[i][j + 1]:
            ans += int(grid[i][j]) + 1
print(ans)
