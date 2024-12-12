def dfs(r, c, parent):
    global grid, vis
    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == parent:
        grid[r][c] = '.'
        vis.add((r, c))
        up, down, left, right = dfs(r - 1, c, parent), dfs(r + 1, c, parent), dfs(r, c - 1, parent), dfs(r, c + 1, parent)
        return 1 + up[0] + down[0] + left[0] + right[0], up[1] + down[1] + left[1] + right[1]
    if (r, c) in vis:
        return 0, 0
    return 0, 1


grid, total, vis = [list(line.strip()) for line in open('input', 'r')], 0, set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != '.':
            area, perimeter = dfs(i, j, grid[i][j])
            total += area * perimeter
            vis.clear()
print(total)
