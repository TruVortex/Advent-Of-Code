def intersect(nrange):
    global ranges
    for prange in ranges:
        if max(nrange[0], prange[0]) <= min(nrange[1], prange[1]):
            ranges.remove(prange)
            intersect((min(nrange[0], prange[0]), max(nrange[1], prange[1])))
            break
    else:
        ranges.add(nrange)


ranges = set()
for available in open('input', 'r').read().split('\n\n')[0].split('\n'):
    l, r = available.split('-')
    intersect((int(l), int(r)))
print(sum(available[1] - available[0] + 1 for available in ranges))
