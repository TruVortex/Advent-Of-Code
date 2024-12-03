import re

total = 0
on = True
for line in open('input', 'r'):
    for instruction in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line):
        if instruction.startswith('mul'):
            total += on * int(instruction[4:].split(',')[0]) * int(instruction[4:-1].split(',')[1])
        else:
            on = instruction == 'do()'
print(total)
