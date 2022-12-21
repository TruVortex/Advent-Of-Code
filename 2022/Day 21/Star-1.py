commands = open('input', 'r').read().splitlines()
lookup = {}
for command in commands:
    if command[-1].isdigit():
        lookup[command[:4]] = int(command[6:])
    elif command[6:10] in lookup and command[13:] in lookup:
        lookup[command[:4]] = eval(f'lookup["{command[6:10]}"]{command[11]}lookup["{command[13:]}"]')
    else:
        commands.append(command)
print(lookup['root'])
