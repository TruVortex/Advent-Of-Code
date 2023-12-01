import re

summate = 0
for line in open('input', 'r').read().splitlines():
    line = re.sub('\D', '', line)
    summate += int(line[0]) * 10 + int(line[-1])
print(summate)
