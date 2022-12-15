# Takes a long time to run
input = open('input', 'r')
lines = [line.split() for line in input.read().splitlines()]
for y in range(4000001):
    groups_1, groups_2 = [], []
    for line in lines:
        sx, sy, bx, by = int(line[2][2:-1]), int(line[3][2:-1]), int(line[8][2:-1]), int(line[9][2:])
        dist = abs(bx - sx) + abs(by - sy) - abs(y - sy)
        if dist < 0:
            continue
        groups_1.append((sx - dist, sx + dist))
    groups_1.sort()
    for left, right in groups_1:
        if not groups_2 or left > groups_2[-1][1] + 1:
            groups_2.append([left, right])
        else:
            groups_2[-1][1] = max(groups_2[-1][1], right)
    x = 0
    for left, right in groups_2:
        if x < left:
            print(4000000 * x + y)
            exit(0)
        x = right + 1
        if x > 4000000:
            break
