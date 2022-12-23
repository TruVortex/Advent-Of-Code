from collections import defaultdict
from operator import itemgetter

elves, moves, consider = [], ((-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)), [0, 1, 2, 3]
for y, line in enumerate(open('input', 'r')):
    for x, char in enumerate(line):
        if char == '#':
            elves.append((x, y))
for i in range(10):
    propose = []
    freq = defaultdict(int)
    for elf in elves:
        possible = [elf] * 4
        if all((elf[0] + move[0], elf[1] + move[1]) not in elves for move in moves):
            propose.append(elf)
            continue
        if all((elf[0] + move[0], elf[1] + move[1]) not in elves for move in moves[:3]):
            possible[0] = (elf[0], elf[1] - 1)
        if all((elf[0] + move[0], elf[1] + move[1]) not in elves for move in moves[4:7]):
            possible[1] = (elf[0], elf[1] + 1)
        if all((elf[0] + move[0], elf[1] + move[1]) not in elves for move in moves[6:]):
            possible[2] = (elf[0] - 1, elf[1])
        if all((elf[0] + move[0], elf[1] + move[1]) not in elves for move in moves[2:5]):
            possible[3] = (elf[0] + 1, elf[1])
        for j in range(4):
            if possible[consider[j]] != elf:
                propose.append(possible[consider[j]])
                freq[propose[-1]] += 1
                break
        else:
            propose.append(elf)
    for j in range(len(elves)):
        if freq[propose[j]] <= 1:
            elves[j] = propose[j]
    consider = consider[1:] + [consider[0]]
print((max(elves)[0] - min(elves)[0] + 1) * (max(elves, key=itemgetter(1))[1] - min(elves, key=itemgetter(1))[1] + 1) - len(elves))
