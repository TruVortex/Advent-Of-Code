import operator
import re


def get(val):
    global values
    if val.isnumeric():
        return val
    return (val in values) and values[val]


instructions = open('input', 'r').read().splitlines()
values = {}
while instructions:
    for i in range(len(instructions) - 1, -1, -1):
        instruction = re.match(r'(\w+)\s?(\w+)?\s?(\w+)? -> (\w+)', instructions[i]).groups()
        if instruction[1] == instruction[2] and get(instruction[0]):
            values[instruction[3]] = get(instruction[0])
            instructions.pop(i)
        elif instruction[0] == 'NOT' and get(instruction[1]):
            values[instruction[3]] = str(int(get(instruction[1])) ^ 0xffff)
            instructions.pop(i)
        elif get(instruction[0]) and get(instruction[2]):
            values[instruction[3]] = str({'AND': operator.and_, 'OR': operator.or_, 'LSHIFT': operator.lshift, 'RSHIFT': operator.rshift}[instruction[1]](int(get(instruction[0])), int(get(instruction[2]))))
            instructions.pop(i)
print(values['a'])
