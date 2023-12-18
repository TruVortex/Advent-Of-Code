cur, vis, direction = (0, 0), [[False] * 1000 for _ in range(1000)], {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
for line in open('input', 'r'):
    line = line.split()
    for _ in range(int(line[1])):
        cur = (cur[0] + direction[line[0]][0], cur[1] + direction[line[0]][1])
        vis[cur[0] + 500][cur[1] + 500] = True
q = [(501, 501)]
while q:
    cur = q[-1]
    q.pop()
    for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        if not vis[cur[0] + dx][cur[1] + dy]:
            q.append((cur[0] + dx, cur[1] + dy))
            vis[cur[0] + dx][cur[1] + dy] = True
print(sum(row.count(True) for row in vis))
