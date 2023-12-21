from collections import deque

grid = ['#' + line.strip() + '#' for line in open('input', 'r')]
grid = ['#' * len(grid[0])] + grid + ['#' * len(grid[0])]
q = None
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'S':
            q = [(y, x)]
for _ in range(64):
    new_q = set()
    for cur in q:
        for dy, dx in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            if grid[cur[0] + dy][cur[1] + dx] != '#':
                new_q.add((cur[0] + dy, cur[1] + dx))
    q = new_q
print(len(q))
