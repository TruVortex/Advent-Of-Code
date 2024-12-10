def dfs(r, c, cur):
    global grid
    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and int(grid[r][c]) == cur:
        if cur == 9:
            return 1
        return dfs(r - 1, c, cur + 1) + dfs(r + 1, c, cur + 1) + dfs(r, c - 1, cur + 1) + dfs(r, c + 1, cur + 1)
    return 0


grid, total = open('input', 'r').read().split(), 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '0':
            total += dfs(i, j, 0)
print(total)
