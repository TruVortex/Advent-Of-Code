import re

summate = 0
for line in open('input', 'r'):
    line = re.sub(r'\D', '', line)
    summate += int(line[0]) * 10 + int(line[-1])
print(summate)
