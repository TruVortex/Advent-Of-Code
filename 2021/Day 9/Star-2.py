from math import prod
from queue import Queue

input = open('input', 'r')
grid, vis, basins = ['9' * 150] + input.read().split() + ['9' * 150], [[False for i in range(150)] for j in range(
    150)], []
for i in range(len(grid)):
    grid[i] = '9' + grid[i] + '9'
for i in range(1, len(grid)):
    for j in range(1, len(grid[1])):
        if grid[i][j] < grid[i - 1][j] and grid[i][j] < grid[i + 1][j] and grid[i][j] < grid[i][j - 1] and grid[i][j]\
                < grid[i][j + 1]:
            q = Queue()
            q.put((i, j))
            size = 1
            while not q.empty():
                cur = q.get()
                if not vis[cur[0] - 1][cur[1]] and 9 > int(grid[cur[0] - 1][cur[1]]) > int(grid[cur[0]][cur[1]]):
                    size += 1
                    q.put((cur[0] - 1, cur[1]))
                    vis[cur[0] - 1][cur[1]] = True
                if not vis[cur[0] + 1][cur[1]] and 9 > int(grid[cur[0] + 1][cur[1]]) > int(grid[cur[0]][cur[1]]):
                    size += 1
                    q.put((cur[0] + 1, cur[1]))
                    vis[cur[0] + 1][cur[1]] = True
                if not vis[cur[0]][cur[1] - 1] and 9 > int(grid[cur[0]][cur[1] - 1]) > int(grid[cur[0]][cur[1]]):
                    size += 1
                    q.put((cur[0], cur[1] - 1))
                    vis[cur[0]][cur[1] - 1] = True
                if not vis[cur[0]][cur[1] + 1] and 9 > int(grid[cur[0]][cur[1] + 1]) > int(grid[cur[0]][cur[1]]):
                    size += 1
                    q.put((cur[0], cur[1] + 1))
                    vis[cur[0]][cur[1] + 1] = True
            basins.append(size)
print(prod(sorted(basins)[-3:]))
