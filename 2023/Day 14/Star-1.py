def tilt(direction):
    global grid
    if direction == 'N':
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i] == 'O':
                    for k in range(j, -1, -1):
                        if grid[k - 1][i] in 'O#@':
                            grid[j][i] = '.'
                            grid[k][i] = 'O'
                            break
    elif direction == 'S':
        for i in range(len(grid[0])):
            for j in range(len(grid) - 1, -1, -1):
                if grid[j][i] == 'O':
                    for k in range(j, len(grid)):
                        if grid[k + 1][i] in 'O#@':
                            grid[j][i] = '.'
                            grid[k][i] = 'O'
                            break
    elif direction == 'W':
        for row in grid:
            for i in range(len(row)):
                if row[i] == 'O':
                    for j in range(i, -1, -1):
                        if row[j - 1] in 'O#':
                            row[i] = '.'
                            row[j] = 'O'
                            break
    else:
        for row in grid:
            for i in range(len(row) - 1, -1, -1):
                if row[i] == 'O':
                    for j in range(i, len(row)):
                        if row[j + 1] in 'O#':
                            row[i] = '.'
                            row[j] = 'O'
                            break


grid = [list('#' + line.strip() + '#') for line in open('input', 'r')]
grid = [['#'] * len(grid[0])] + grid + [['#'] * len(grid[0])]
tilt('N')
print(sum(grid[i].count('O') * (len(grid) - i - 1) for i in range(len(grid))))
