import sys
import threading

sys.setrecursionlimit(8000)

input = open('input', 'r')
grid, vis = [[['.' for i in range(21)] for j in range(21)] for k in range(21)], [[[0 for i in range(21)] for j in range(21)] for k in range(21)]
cur, moves = 0, ((0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0))
for line in input:
    coords = list(map(int, line.split(',')))
    grid[coords[0]][coords[1]][coords[2]] = 'D'


def floodfill(x, y, z, fill):
    global cur
    if fill > 0:
        if grid[x][y][z] == 'D':
            return
        vis[x][y][z] = fill
        cur += 1
        for move in moves:
            if all(0 <= element <= 20 for element in (x + move[0], y + move[1], z + move[2])) and not vis[x + move[0]][y + move[1]][z + move[2]]:
                floodfill(x + move[0], y + move[1], z + move[2], fill)
    else:
        if grid[x][y][z] == '.':
            return vis[x][y][z] == -fill
        vis[x][y][z] = 1000
        curr = 0
        for move in moves:
            if vis[x + move[0]][y + move[1]][z + move[2]] != 1000:
                curr += floodfill(x + move[0], y + move[1], z + move[2], fill)
        return curr


ans, cnt, maxx = 0, 1, (0, 0)
for i in range(21):
    for j in range(21):
        for k in range(21):
            if grid[i][j][k] == '.' and not vis[i][j][k]:
                cur = 0
                threading.stack_size(67108864)
                thread = threading.Thread(target=floodfill, args=(i, j, k, cnt))
                thread.start()
                thread.join()
                if cur > maxx[1]:
                    maxx = (cnt, cur)
                cnt += 1
for i in range(21):
    for j in range(21):
        for k in range(21):
            if grid[i][j][k] == 'D' and not vis[i][j][k]:
                ans += floodfill(i, j, k, -maxx[0])
print(ans)
