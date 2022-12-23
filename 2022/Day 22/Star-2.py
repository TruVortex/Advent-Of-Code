import re

grid, moves = map(str.splitlines, open('input', 'r').read().split('\n\n'))
cur, move, length = [0, 0], [0, 1], max(map(len, grid))
moves, grid = moves[0], [line + ' ' * (length - len(line)) for line in grid]
while grid[cur[0]][cur[1]] != '.':
    cur[1] += 1
for dist, turn in re.findall(r'(\d+)([RL]?)', moves):
    for i in range(int(dist)):
        new, new_move = [cur[0] + move[0], cur[1] + move[1]], move.copy()
        if new[0] < 50 and new[1] < 50:
            new_move = [0, 1]
            new = [149 - new[0], 0]
        elif new[1] < 0 and 100 <= new[0] < 150:
            new_move = [0, 1]
            new = [149 - new[0], 50]
        elif new[1] < 50 <= new[0] < 100:
            if move == [0, -1]:
                new_move = [1, 0]
                new = [100, new[0] - 50]
            else:
                new_move = [0, 1]
                new = [new[1] + 50, 50]
        elif 50 <= new[0] < 100 <= new[1]:
            if move == [1, 0]:
                new_move = [0, -1]
                new = [new[1] - 50, 99]
            else:
                new_move = [-1, 0]
                new = [49, new[0] + 50]
        elif new[1] >= 150:
            new_move = [0, -1]
            new = [149 - new[0], 99]
        elif 100 <= new[0] < 150 and 100 <= new[1]:
            new_move = [0, -1]
            new = [149 - new[0], 149]
        elif new[0] >= 150 and new[1] >= 50:
            if move == [1, 0]:
                new_move = [0, -1]
                new = [new[1] + 100, 49]
            else:
                new_move = [-1, 0]
                new = [149, new[0] - 100]
        elif new[0] < 0 and new[1] >= 100:
            new = [199, new[1] - 100]
        elif new[0] >= 200:
            new = [0, new[1] + 100]
        elif new[0] < 0 and 50 <= new[1] < 100:
            new_move = [0, 1]
            new = [new[1] + 100, 0]
        elif 150 <= new[0] < 200 and new[1] < 0:
            new_move = [1, 0]
            new = [0, new[0] - 100]
        if grid[new[0]][new[1]] == '#':
            break
        cur = new
        move = new_move
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
