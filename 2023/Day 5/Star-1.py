almanac = open('input', 'r').read().split('\n\n')
seeds = list(map(int, almanac[0][6:].split()))
for i in range(1, 8):
    ranges = almanac[i].split('\n')
    change = [False] * len(seeds)
    for j in range(1, len(ranges)):
        cur = list(map(int, ranges[j].split()))
        for k in range(len(seeds)):
            if not change[k] and cur[1] <= seeds[k] < cur[1] + cur[2]:
                seeds[k] = seeds[k] + cur[0] - cur[1]
                change[k] = True
print(min(seeds))
