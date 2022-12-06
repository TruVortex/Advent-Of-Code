from queue import Queue

input = open('input', 'r')
grid = []
for line in input:
    grid.append([int(char) for char in line.strip()])
moves = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1))
for i in range(1000):
    q = Queue()
    for j in range(len(grid)):
        for k in range(len(grid[0])):
            grid[j][k] += 1
            if grid[j][k] == 10:
                q.put((j, k))
    while not q.empty():
        cur = q.get()
        for move in moves:
            if 0 <= cur[0] + move[0] < len(grid) and 0 <= cur[1] + move[1] < len(grid[0]):
                grid[cur[0] + move[0]][cur[1] + move[1]] += 1
                if grid[cur[0] + move[0]][cur[1] + move[1]] == 10:
                    q.put((cur[0] + move[0], cur[1] + move[1]))
    cnt = 0
    for j in range(len(grid)):
        for k in range(len(grid[0])):
            if grid[j][k] >= 10:
                cnt += 1
                grid[j][k] = 0
    if cnt == len(grid) * len(grid[0]):
        print(i + 1)
        break
