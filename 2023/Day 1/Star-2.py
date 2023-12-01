import re

summate = 0
for line in open('input', 'r').read().splitlines():
    new_line = ''
    for i in range(len(line)):
        if line[i:i + 3] == 'one':
            new_line += '1'
        elif line[i:i + 3] == 'two':
            new_line += '2'
        elif line[i:i + 5] == 'three':
            new_line += '3'
        elif line[i:i + 4] == 'four':
            new_line += '4'
        elif line[i:i + 4] == 'five':
            new_line += '5'
        elif line[i:i + 3] == 'six':
            new_line += '6'
        elif line[i:i + 5] == 'seven':
            new_line += '7'
        elif line[i:i + 5] == 'eight':
            new_line += '8'
        elif line[i:i + 4] == 'nine':
            new_line += '9'
        else:
            new_line += line[i]
    new_line = re.sub('\D', '', new_line)
    summate += int(new_line[0]) * 10 + int(new_line[-1])
print(summate)
