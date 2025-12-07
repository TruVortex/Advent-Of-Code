splitters, cnt = open('input', 'r').read().split(), 0
beams = {splitters[0].find('S')}
for line in splitters[1:]:
    nbeams = set()
    for beam in beams:
        if line[beam] == '^':
            nbeams.add(beam - 1)
            nbeams.add(beam + 1)
            cnt += 1
        else:
            nbeams.add(beam)
    beams = nbeams
print(cnt)
