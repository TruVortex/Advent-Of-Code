from collections import defaultdict

splitters, total = open('input', 'r').read().split(), 1
beams = {splitters[0].find('S'): 1}
for line in splitters[1:]:
    nbeams = defaultdict(int)
    for beam, cnt in beams.items():
        if line[beam] == '^':
            nbeams[beam - 1] += cnt
            nbeams[beam + 1] += cnt
            total += cnt
        else:
            nbeams[beam] += cnt
    beams = nbeams
print(total)
