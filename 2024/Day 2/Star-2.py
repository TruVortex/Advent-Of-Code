from math import copysign

cnt = 0
for line in open('input', 'r'):
    levels = list(map(int, line.split()))
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        positive = copysign(1, new_levels[1] - new_levels[0]) == 1
        for j in range(1, len(new_levels)):
            if (positive and (new_levels[j] - new_levels[j - 1] < 1 or new_levels[j] - new_levels[j - 1] > 3)) or (not positive and (new_levels[j] - new_levels[j - 1] < -3 or new_levels[j] - new_levels[j - 1] > -1)):
                break
        else:
            cnt += 1
            break
print(cnt)
