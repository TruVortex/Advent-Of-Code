import re

total = 0
for line in open('input', 'r'):
    for instruction in re.findall(r'(?<=mul\()\d+,\d+(?=\))', line):
        total += int(instruction.split(',')[0]) * int(instruction.split(',')[1])
print(total)
