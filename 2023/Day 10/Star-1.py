grid, start, cur, dirs = [], None, None, {'left': ['-', 'L', 'F'], 'right': ['-', 'J', '7'], 'down': ['|', 'L', 'J'], 'up': ['|', '7', 'F']}
for i, line in enumerate(open('input', 'r')):
    grid.append(['.'])
    for j, char in enumerate(line.strip()):
        if char == 'S':
            start = [i + 1, j + 1]
            cur = [i + 1, j + 1]
        grid[-1].append(char)
    grid[-1].append('.')
grid = ['.' * len(grid[0])] + grid + ['.' * len(grid[0])]
if grid[start[0]][start[1] - 1] in dirs['left'] and grid[start[0]][start[1] + 1] in dirs['right']:
    grid[start[0]][start[1]] = '-'
    cur[1] -= 1
elif grid[start[0]][start[1]] in dirs['down'] and grid[start[0] - 1][start[1]] in dirs['up']:
    grid[start[0] + 1][start[1]] = '|'
    cur[0] += 1
elif grid[start[0]][start[1] + 1] in dirs['right'] and grid[start[0] - 1][start[1]] in dirs['up']:
    grid[start[0]][start[1]] = 'L'
    cur[1] += 1
elif grid[start[0]][start[1] - 1] in dirs['left'] and grid[start[0] - 1][start[1]] in dirs['up']:
    grid[start[0]][start[1]] = 'J'
    cur[1] -= 1
elif grid[start[0]][start[1] - 1] in dirs['left'] and grid[start[0] + 1][start[1]] in dirs['down']:
    grid[start[0]][start[1]] = '7'
    cur[1] -= 1
else:
    grid[start[0]][start[1]] = 'F'
    cur[1] += 1
cnt, vis = 1, [[False] * len(grid[0]) for _ in range(len(grid))]
vis[start[0]][start[1]] = vis[cur[0]][cur[1]] = True
while cur != start:
    if grid[cur[0]][cur[1]] == '-':
        if vis[cur[0]][cur[1] - 1]:
            cur[1] += 1
        else:
            cur[1] -= 1
    elif grid[cur[0]][cur[1]] == '|':
        if vis[cur[0] - 1][cur[1]]:
            cur[0] += 1
        else:
            cur[0] -= 1
    elif grid[cur[0]][cur[1]] == 'L':
        if vis[cur[0]][cur[1] + 1]:
            cur[0] -= 1
        else:
            cur[1] += 1
    elif grid[cur[0]][cur[1]] == 'J':
        if vis[cur[0]][cur[1] - 1]:
            cur[0] -= 1
        else:
            cur[1] -= 1
    elif grid[cur[0]][cur[1]] == '7':
        if vis[cur[0]][cur[1] - 1]:
            cur[0] += 1
        else:
            cur[1] -= 1
    else:
        if vis[cur[0]][cur[1] + 1]:
            cur[0] += 1
        else:
            cur[1] += 1
    cnt += 1
    vis[cur[0]][cur[1]] = True
    vis[start[0]][start[1]] = False
print(cnt // 2)
