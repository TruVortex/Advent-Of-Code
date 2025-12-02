ranges, total = open('input', 'r').readline().split(','), 0
for nrange in ranges:
    start, end = list(map(int, nrange.split('-')))
    for num in range(start, end + 1):
        snum = str(num)
        if (snum + snum).find(snum, 1, -1) != -1:
            total += num
print(total)
