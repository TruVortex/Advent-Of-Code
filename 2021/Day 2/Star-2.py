input = open('input', 'r')
commands = input.read().split('\n')
depth = pos = aim = 0
for command in commands:
    if command[0] == 'f':
        pos += int(command[8:])
        depth += aim * int(command[8:])
    elif command[0] == 'd':
        aim += int(command[5:])
    else:
        aim -= int(command[3:])
print(depth * pos)
