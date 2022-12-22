import re

grid, moves = map(str.splitlines, open('input', 'r').read().split('\n\n'))
cur, move, length = [0, 0], [0, 1], max(map(len, grid))
moves, grid = moves[0], [line + ' ' * (length - len(line)) for line in grid]
while grid[cur[0]][cur[1]] != '.':
    cur[1] += 1
for dist, turn in re.findall(r'(\d+)([RL]?)', moves):
    for i in range(int(dist)):
        new = [(cur[0] + move[0]) % len(grid), (cur[1] + move[1]) % len(grid[0])]
        while grid[new[0]][new[1]] == ' ':
            new[0] = (new[0] + move[0]) % len(grid)
            new[1] = (new[1] + move[1]) % len(grid[0])
        if grid[new[0]][new[1]] == '#':
            break
        cur = new
    if turn == 'L':
        move[0], move[1] = -move[1], move[0]
    elif turn == 'R':
        move[0], move[1] = move[1], -move[0]
if move == [0, 1]:
    print(1000 * (cur[0] + 1) + 4 * (cur[1] + 1))
elif move == [1, 0]:
    print(1000 * (cur[0] + 1) + 4 * (cur[1] + 1) + 1)
elif move == [0, -1]:
    print(1000 * (cur[0] + 1) + 4 * (cur[1] + 1) + 2)
else:
    print(1000 * (cur[0] + 1) + 4 * (cur[1] + 1) + 3)
