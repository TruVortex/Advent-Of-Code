input = open('input', 'r')
floor = [[0 for i in range(1000)] for j in range(1000)]
vents = []
for line in input:
    vents.append(list(map(int, line.replace(' -> ', ',').split(','))))
for vent in vents:
    if vent[0] == vent[2]:
        if vent[1] > vent[3]:
            vent[1], vent[3] = vent[3], vent[1]
        for i in range(vent[1], vent[3] + 1):
            floor[vent[0]][i] += 1
    elif vent[1] == vent[3]:
        if vent[0] > vent[2]:
            vent[0], vent[2] = vent[2], vent[0]
        for i in range(vent[0], vent[2] + 1):
            floor[i][vent[1]] += 1
    else:
        if vent[0] > vent[2]:
            vent[0], vent[2] = vent[2], vent[0]
            vent[1], vent[3] = vent[3], vent[1]
        mult = 1
        if vent[1] > vent[3]:
            mult = -1
        for i in range(vent[0], vent[2] + 1):
            floor[i][vent[1] + mult * (i - vent[0])] += 1
ans = 0
for i in range(1000):
    for j in range(1000):
        if floor[i][j] >= 2:
            ans += 1
print(ans)
