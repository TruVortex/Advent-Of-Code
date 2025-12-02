ranges, total = open('input', 'r').readline().split(','), 0
for nrange in ranges:
    start, end = list(map(int, nrange.split('-')))
    for num in range(start, end + 1):
        snum = str(num)
        if len(snum) % 2 == 0 and snum[:len(snum) // 2] == snum[len(snum) // 2:]:
            total += num
print(total)
