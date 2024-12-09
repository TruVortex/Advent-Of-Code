line, block_ranges, ranges, cnt, total = list(map(int, list(open('input', 'r').readline().strip()))), [], [], 0, 0
for i, blocks in enumerate(line):
    if i % 2:
        ranges.append([cnt, blocks])
    else:
        block_ranges.append([cnt, blocks, i // 2])
    cnt += blocks
for i in range(len(block_ranges) - 1, -1, -1):
    for j in range(len(ranges)):
        if ranges[j][0] < block_ranges[i][0] and block_ranges[i][1] <= ranges[j][1]:
            block_ranges[i][0] = ranges[j][0]
            ranges[j][0] += block_ranges[i][1]
            ranges[j][1] -= block_ranges[i][1]
            break
for block in block_ranges:
    for i in range(block[0], block[0] + block[1]):
        total += block[2] * i
print(total)
