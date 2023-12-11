from copy import deepcopy

grid = [list('.' + line.strip() + '.') for line in open('input', 'r')]
grid, move = [['.'] * len(grid[0])] + grid + [['.'] * len(grid[0])], ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
for _ in range(100):
    new = deepcopy(grid)
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            cnt = 0
            for dy, dx in move:
                cnt += grid[i + dy][j + dx] == '#'
            if grid[i][j] == '#':
                new[i][j] = '#' if 2 <= cnt <= 3 else '.'
            else:
                new[i][j] = '#' if cnt == 3 else '.'
    grid = new
    grid[1][1] = grid[-2][1] = grid[1][-2] = grid[-2][-2] = '#'
print(sum(line.count('#') for line in grid))
