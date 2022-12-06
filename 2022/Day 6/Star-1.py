input = open('input', 'r')
line = input.readline().strip()
for i in range(len(line) - 5):
    if len({line[i], line[i + 1], line[i + 2], line[i + 3]}) == 4:
        print(i + 4)
        break
