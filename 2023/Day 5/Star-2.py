almanac = open('input', 'r').read().split('\n\n')
seed_ranges = list(map(int, almanac[0][6:].split()))
seeds = []
for i in range(0, len(seed_ranges), 2):
    seeds.append((seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]))
for i in range(1, 8):
    ranges = almanac[i].split('\n')
    new = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        for j in range(1, len(ranges)):
            cur = list(map(int, ranges[j].split()))
            range_start, range_end = max(start, cur[1]), min(end, cur[1] + cur[2])
            if range_start < range_end:
                new.append((range_start + cur[0] - cur[1], range_end + cur[0] - cur[1]))
                if range_start > start:
                    seeds.append((start, range_start))
                if end > range_end:
                    seeds.append((range_end, end))
                break
        else:
            new.append((start, end))
    seeds = new
print(min(seeds)[0])
