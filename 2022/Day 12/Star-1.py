from queue import Queue

grid = [list(line) for line in open('input', 'r').read().splitlines()]
vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
start_x = start_y = end_x = end_y = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            grid[i][j] = 'a'
            start_x, start_y = i, j
        elif grid[i][j] == 'E':
            grid[i][j] = 'z'
            end_x, end_y = i, j
q = Queue()
q.put((start_x, start_y, 0))
vis[start_x][start_y] = True
moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
while not q.empty():
    x, y, dist = q.get()
    if x == end_x and y == end_y:
        print(dist)
        break
    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and not vis[new_x][new_y] and ord(grid[new_x][new_y]) - ord(grid[x][y]) <= 1:
            vis[new_x][new_y] = True
            q.put((new_x, new_y, dist + 1))
