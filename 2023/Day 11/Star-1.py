universe = [line.strip() for line in open('input', 'r')]
rows, columns, galaxies = [], [], []
for i, line in enumerate(universe):
    if all(ch == '.' for ch in line):
        rows.append(i)
for i in range(len(universe[0])):
    flag = True
    for j in range(len(universe)):
        flag &= universe[j][i] == '.'
        if universe[j][i] == '#':
            galaxies.append((j, i))
    if flag:
        columns.append(i)
summate = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        cnt = 0
        for row in rows:
            if min(galaxies[i][0], galaxies[j][0]) <= row <= max(galaxies[i][0], galaxies[j][0]):
                cnt += 1
        for column in columns:
            if min(galaxies[i][1], galaxies[j][1]) <= column <= max(galaxies[i][1], galaxies[j][1]):
                cnt += 1
        summate += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1]) + cnt
print(summate)
