def check(x, y):
    global grid
    return sum(grid[x + dx][y + dy] == '@' for (dx, dy) in dirs) < 4


grid, dirs, q, cnt = [list('.' + line.strip() + '.') for line in open('input', 'r')], ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)), [], 0
grid = ['.' * len(grid[0])] + grid + ['.' * len(grid[0])]
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        if grid[i][j] == '@' and check(i, j):
            q.append((i, j))
while q:
    cur = q.pop()
    grid[cur[0]][cur[1]] = '.'
    cnt += 1
    for (dx, dy) in dirs:
        if grid[nx := cur[0] + dx][ny := cur[1] + dy] == '@' and (nx, ny) not in q and check(nx, ny):
            q.append((nx, ny))
print(cnt)
