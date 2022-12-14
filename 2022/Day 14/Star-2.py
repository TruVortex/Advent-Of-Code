input = open('input', 'r')
floor, grid = 0, [[False for i in range(200)] for j in range(700)]
for line in input:
    points = list(map(eval, line.split(' -> ')))
    for i in range(1, len(points)):
        if points[i - 1][0] == points[i][0]:
            for j in range(min(points[i - 1][1], points[i][1]), max(points[i - 1][1], points[i][1]) + 1):
                grid[points[i][0]][j] = True
                floor = max(floor, j + 1)
        else:
            for j in range(min(points[i - 1][0], points[i][0]), max(points[i - 1][0], points[i][0]) + 1):
                grid[j][points[i][1]] = True
                floor = max(floor, points[i][1] + 1)
cnt = 0
while not grid[500][0]:
    point = [500, 0]
    while True:
        if point[1] >= floor:
            break
        elif not grid[point[0]][point[1] + 1]:
            point[1] += 1
            continue
        elif not grid[point[0] - 1][point[1] + 1]:
            point[0] -= 1
            point[1] += 1
            continue
        elif not grid[point[0] + 1][point[1] + 1]:
            point[0] += 1
            point[1] += 1
            continue
        break
    grid[point[0]][point[1]] = True
    cnt += 1
print(cnt)
