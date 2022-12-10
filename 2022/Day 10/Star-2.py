input = open('input', 'r')
register, values = 1, []
for line in input:
    values.append(register)
    if line[0] == 'a':
        values.append(register)
        register += int(line.split()[1])
for i in range(0, len(values), 40):
    for j in range(40):
        print('#' if abs(values[i + j] - j) <= 1 else ' ', end='')
    print()
