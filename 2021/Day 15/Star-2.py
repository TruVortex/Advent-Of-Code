import copy
import heapq

cavern = []
for i in range(5):
    cavern += [[0] + list(map(int, line.strip() * 5)) + [0] for line in open('input', 'r')]
cavern = [[0] * len(cavern[0])] + cavern + [[0] * len(cavern[0])]
for i in range(1, len(cavern) - 1):
    for j in range(1, len(cavern[0]) - 1):
        cavern[i][j] = (cavern[i][j] - 1 + 5 * (i - 1) // (len(cavern) - 2) + 5 * (j - 1) // (len(cavern[0]) - 2)) % 9 + 1
moves = ((0, -1), (0, 1), (-1, 0), (1, 0))
vis = [[0] * len(cavern[0]) for _ in range(len(cavern))]
vis[1][1] = 1
q = [(0, 1, 1)]
while q:
    cur = q[0]
    heapq.heappop(q)
    if cur[1] == len(vis) - 2 and cur[2] == len(vis[0]) - 2:
        print(cur[0])
        break
    for move in moves:
        nx, ny = cur[1] + move[0], cur[2] + move[1]
        if cavern[nx][ny] and not vis[nx][ny]:
            vis[nx][ny] = 1
            heapq.heappush(q, (cur[0] + cavern[nx][ny], nx, ny))
