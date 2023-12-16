mirrors, maximum = [line.strip() for line in open('input', 'r')], 0
for _ in range(len(mirrors) * 2 + len(mirrors[0]) * 2):
    energize = [[[] for i in range(len(mirrors[0]))] for j in range(len(mirrors))]
    beams = []
    if _ < len(mirrors):
        beams.append((_, 0, 2))
    elif _ < 2 * len(mirrors):
        beams.append((_ - len(mirrors), len(mirrors[0]) - 1, 4))
    elif _ < 2 * len(mirrors) + len(mirrors[0]):
        beams.append((0, _ - 2 * len(mirrors), 3))
    else:
        beams.append((len(mirrors) - 1, _ - 2 * len(mirrors) - len(mirrors[0]), 1))
    while beams:
        beam = beams[0]
        beams.pop(0)
        if 0 > beam[0] or beam[0] >= len(mirrors) or 0 > beam[1] or beam[1] >= len(mirrors[1]) or beam[2] in energize[beam[0]][beam[1]]:
            continue
        energize[beam[0]][beam[1]].append(beam[2])
        if beam[2] == 1:
            if mirrors[beam[0]][beam[1]] in '/-':
                beams.append((beam[0], beam[1] + 1, 2))
            if mirrors[beam[0]][beam[1]] in '\\-':
                beams.append((beam[0], beam[1] - 1, 4))
            if mirrors[beam[0]][beam[1]] in '.|':
                beams.append((beam[0] - 1, beam[1], 1))
        elif beam[2] == 2:
            if mirrors[beam[0]][beam[1]] in '/|':
                beams.append((beam[0] - 1, beam[1], 1))
            if mirrors[beam[0]][beam[1]] in '\\|':
                beams.append((beam[0] + 1, beam[1], 3))
            if mirrors[beam[0]][beam[1]] in '.-':
                beams.append((beam[0], beam[1] + 1, 2))
        elif beam[2] == 3:
            if mirrors[beam[0]][beam[1]] in '/-':
                beams.append((beam[0], beam[1] - 1, 4))
            if mirrors[beam[0]][beam[1]] in '\\-':
                beams.append((beam[0], beam[1] + 1, 2))
            if mirrors[beam[0]][beam[1]] in '.|':
                beams.append((beam[0] + 1, beam[1], 3))
        elif beam[2] == 4:
            if mirrors[beam[0]][beam[1]] in '/|':
                beams.append((beam[0] + 1, beam[1], 3))
            if mirrors[beam[0]][beam[1]] in '\\|':
                beams.append((beam[0] - 1, beam[1], 1))
            if mirrors[beam[0]][beam[1]] in '.-':
                beams.append((beam[0], beam[1] - 1, 4))
    maximum = max(maximum, sum(sum(len(element) > 0 for element in row) for row in energize))
print(maximum)
