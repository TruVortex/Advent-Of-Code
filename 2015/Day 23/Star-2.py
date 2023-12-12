cur, a, b, instructions = 0, 1, 0, [line.replace(',', '').split() for line in open('input', 'r')]
while cur < len(instructions):
    if instructions[cur][0][0] != 'j':
        if instructions[cur][0] == 'hlf':
            exec(f'{instructions[cur][1]} //= 2')
        elif instructions[cur][0] == 'tpl':
            exec(f'{instructions[cur][1]} *= 3')
        else:
            exec(f'{instructions[cur][1]} += 1')
        cur += 1
    elif instructions[cur][0] == 'jmp':
        cur += int(instructions[cur][1])
    elif instructions[cur][0] == 'jie':
        exec(f'cur += max(1, (1 - {instructions[cur][1]} % 2) * {instructions[cur][2]})')
    else:
        exec(f'cur += max(1, ({instructions[cur][1]} == 1) * {instructions[cur][2]})')
print(b)
