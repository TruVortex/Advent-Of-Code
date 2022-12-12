from queue import Queue

grid = [list(line) for line in open('input', 'r').read().splitlines()]
vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
end_x = end_y = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            grid[i][j] = 'a'
        elif grid[i][j] == 'E':
            grid[i][j] = 'z'
            end_x, end_y = i, j
q = Queue()
q.put((end_x, end_y, 0))
vis[end_x][end_y] = True
moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
while not q.empty():
    x, y, dist = q.get()
    if grid[x][y] == 'a':
        print(dist)
        break
    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and not vis[new_x][new_y] and ord(grid[x][y]) - ord(grid[new_x][new_y]) <= 1:
            vis[new_x][new_y] = True
            q.put((new_x, new_y, dist + 1))
