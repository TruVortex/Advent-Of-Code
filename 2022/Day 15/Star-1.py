input = open('input', 'r')
beacons, impossible, groups = set(), set(), []
for line in input:
    line = line.split()
    sx, sy, bx, by = int(line[2][2:-1]), int(line[3][2:-1]), int(line[8][2:-1]), int(line[9][2:])
    dist = abs(bx - sx) + abs(by - sy) - abs(2000000 - sy)
    if dist < 0:
        continue
    groups.append((sx - dist, sx + dist))
    if by == 2000000:
        beacons.add(bx)
for left, right in groups:
    for x in range(left, right + 1):
        impossible.add(x)
print(len(impossible - beacons))
