import sys

sys.setrecursionlimit(1500)

input = open('input', 'r')
grid, vis = [[['.' for i in range(21)] for j in range(21)] for k in range(21)], [[[False for i in range(21)] for j in range(21)] for k in range(21)]
moves = ((0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0))
for line in input:
    coords = list(map(int, line.split(',')))
    grid[coords[0]][coords[1]][coords[2]] = 'D'


def floodfill(x, y, z):
    if grid[x][y][z] == '.':
        return 1
    vis[x][y][z] = True
    cur = 0
    for move in moves:
        if not vis[x + move[0]][y + move[1]][z + move[2]]:
            cur += floodfill(x + move[0], y + move[1], z + move[2])
    return cur


ans = 0
for i in range(21):
    for j in range(21):
        for k in range(21):
            if grid[i][j][k] == 'D' and not vis[i][j][k]:
                ans += floodfill(i, j, k)
print(ans)
