import sympy

commands = open('input', 'r').read().splitlines()
lookup = {'humn': sympy.Symbol('x')}
for command in commands:
    if command[:4] == 'humn':
        continue
    elif command[-1].isdigit():
        lookup[command[:4]] = int(command[6:])
    elif command[6:10] in lookup and command[13:] in lookup:
        if command[:4] == 'root':
            print(sympy.solve(lookup[command[6:10]] - lookup[command[13:]]))
            exit(0)
        lookup[command[:4]] = eval(f'lookup["{command[6:10]}"]{command[11]}lookup["{command[13:]}"]')
    else:
        commands.append(command)
