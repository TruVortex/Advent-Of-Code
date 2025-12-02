cnt, dial = 0, 50
for line in open('input', 'r'):
    for i in range(int(line[1:])):
        dial += 2 * line.startswith('L') - 1
        dial %= 100
        cnt += dial == 0
print(cnt)
