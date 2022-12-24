grid = open('input', 'r').read().splitlines()
len_x, len_y, cnt, vis, blizzards, moves = len(grid), len(grid[0]), 0, {(0, 1)}, [], {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] in moves:
            blizzards.append((x, y, grid[x][y]))
while (len_x - 1, len_y - 2) not in vis:
    new, new_vis, positions = [], set(), set()
    for x, y, move in blizzards:
        new_x, new_y = x + moves[move][0], y + moves[move][1]
        if new_x == 0:
            new_x = len_x - 2
        elif new_x == len_x - 1:
            new_x = 1
        if new_y == 0:
            new_y = len_y - 2
        elif new_y == len_y - 1:
            new_y = 1
        positions.add((new_x, new_y))
        new.append((new_x, new_y, move))
    for x, y in vis:
        if (x, y) not in positions and grid[x][y] != '#':
            new_vis.add((x, y))
        if (x - 1, y) not in positions and grid[x - 1][y] != '#':
            new_vis.add((x - 1, y))
        if (x + 1, y) not in positions and grid[x + 1][y] != '#':
            new_vis.add((x + 1, y))
        if (x, y - 1) not in positions and grid[x][y - 1] != '#':
            new_vis.add((x, y - 1))
        if (x, y + 1) not in positions and grid[x][y + 1] != '#':
            new_vis.add((x, y + 1))
    blizzards, vis = new, new_vis
    cnt += 1
vis = {(len_x - 1, len_y - 2)}
while (0, 1) not in vis:
    new, new_vis, positions = [], set(), set()
    for x, y, move in blizzards:
        new_x, new_y = x + moves[move][0], y + moves[move][1]
        if new_x == 0:
            new_x = len_x - 2
        elif new_x == len_x - 1:
            new_x = 1
        if new_y == 0:
            new_y = len_y - 2
        elif new_y == len_y - 1:
            new_y = 1
        positions.add((new_x, new_y))
        new.append((new_x, new_y, move))
    for x, y in vis:
        if (x, y) not in positions and grid[x][y] != '#':
            new_vis.add((x, y))
        if (x - 1, y) not in positions and grid[x - 1][y] != '#':
            new_vis.add((x - 1, y))
        if x + 1 < len_x and (x + 1, y) not in positions and grid[x + 1][y] != '#':
            new_vis.add((x + 1, y))
        if (x, y - 1) not in positions and grid[x][y - 1] != '#':
            new_vis.add((x, y - 1))
        if (x, y + 1) not in positions and grid[x][y + 1] != '#':
            new_vis.add((x, y + 1))
    blizzards, vis = new, new_vis
    cnt += 1
vis = {(0, 1)}
while (len_x - 1, len_y - 2) not in vis:
    new, new_vis, positions = [], set(), set()
    for x, y, move in blizzards:
        new_x, new_y = x + moves[move][0], y + moves[move][1]
        if new_x == 0:
            new_x = len_x - 2
        elif new_x == len_x - 1:
            new_x = 1
        if new_y == 0:
            new_y = len_y - 2
        elif new_y == len_y - 1:
            new_y = 1
        positions.add((new_x, new_y))
        new.append((new_x, new_y, move))
    for x, y in vis:
        if (x, y) not in positions and grid[x][y] != '#':
            new_vis.add((x, y))
        if (x - 1, y) not in positions and grid[x - 1][y] != '#':
            new_vis.add((x - 1, y))
        if (x + 1, y) not in positions and grid[x + 1][y] != '#':
            new_vis.add((x + 1, y))
        if (x, y - 1) not in positions and grid[x][y - 1] != '#':
            new_vis.add((x, y - 1))
        if (x, y + 1) not in positions and grid[x][y + 1] != '#':
            new_vis.add((x, y + 1))
    blizzards, vis = new, new_vis
    cnt += 1
print(cnt)
