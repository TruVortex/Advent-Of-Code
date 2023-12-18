cur, vertices, direction, cnt = (0, 0), [], ((1, 0), (0, 1), (-1, 0), (0, -1)), 0
for line in open('input', 'r'):
    line = line.split()
    cur = (cur[0] + int(line[2][2:7], 16) * direction[int(line[2][-2])][0], cur[1] + int(line[2][2:7], 16) * direction[int(line[2][-2])][1])
    vertices.append(cur)
    cnt += int(line[2][2:7], 16)
print(cnt // 2 + 1 + abs(sum(vertices[i][1] * vertices[i - 1][0] - vertices[i][0] * vertices[i - 1][1] for i in range(len(vertices)))) // 2)
