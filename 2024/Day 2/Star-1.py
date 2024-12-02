cnt = 0
for line in open('input', 'r'):
    levels = list(map(int, line.split()))
    positive = levels[0] < levels[1]
    for i in range(1, len(levels)):
        if (positive and (levels[i] - levels[i - 1] < 1 or levels[i] - levels[i - 1] > 3)) or (not positive and (levels[i] - levels[i - 1] < -3 or levels[i] - levels[i - 1] > -1)):
            break
    else:
        cnt += 1
print(cnt)
