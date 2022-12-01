input = open('input', 'r')
commands = input.read().split('\n')
depth = pos = 0
for command in commands:
    if command[0] == 'f':
        pos += int(command[8:])
    elif command[0] == 'd':
        depth += int(command[5:])
    else:
        depth -= int(command[3:])
print(depth * pos)
