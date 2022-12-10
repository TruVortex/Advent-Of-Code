input = open('input', 'r')
ans, register, values = 0, 1, []
for line in input:
    values.append(register)
    if line[0] == 'a':
        values.append(register)
        register += int(line.split()[1])
for i in range(19, len(values), 40):
    ans += (i + 1) * values[i]
print(ans)
