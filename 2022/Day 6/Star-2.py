input = open('input', 'r')
line = input.readline().strip()
for i in range(len(line) - 15):
    cur = set()
    for j in range(14):
        cur.add(line[i + j])
    if len(cur) == 14:
        print(i + 14)
        break
