from queue import Queue

cavern = [[0] + list(map(int, line.strip())) + [0] for line in open('input', 'r')]
cavern = [[0] * len(cavern[0])] + cavern + [[0] * len(cavern[0])]
moves = ((0, -1), (0, 1), (-1, 0), (1, 0))
vis = [[999999999] * len(cavern[0]) for _ in range(len(cavern))]
vis[1][1] = 0
q = Queue()
q.put((1, 1, 0))
while not q.empty():
    cur = q.get()
    for move in moves:
        if cavern[cur[0] + move[0]][cur[1] + move[1]] and cur[2] + cavern[cur[0] + move[0]][cur[1] + move[1]] < vis[cur[0] + move[0]][cur[1] + move[1]]:
            vis[cur[0] + move[0]][cur[1] + move[1]] = cur[2] + cavern[cur[0] + move[0]][cur[1] + move[1]]
            q.put((cur[0] + move[0], cur[1] + move[1], cur[2] + cavern[cur[0] + move[0]][cur[1] + move[1]]))
print(vis[len(vis) - 2][len(vis[0]) - 2])
