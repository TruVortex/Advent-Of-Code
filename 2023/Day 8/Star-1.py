instructions, temp = open('input', 'r').read().split('\n\n')
instructions = list(map(int, instructions.replace('L', '0').replace('R', '1')))
new, cur, end, cnt = temp + '\n', -1, -1, 0
for i in range(len(temp) - 16, -1, -17):
    new = new.replace(temp[i:i + 3], str(i // 17))
    if temp[i:i + 3] == 'AAA':
        cur = i // 17
    elif temp[i:i + 3] == 'ZZZ':
        end = i // 17
nodes = []
while '\n' in new:
    nodes.append(eval(new[new.find('('):new.find('\n')]))
    new = new[new.find('\n') + 1:]
while True:
    for instruction in instructions:
        cur = nodes[cur][instruction]
        cnt += 1
        if cur == end:
            print(cnt)
            exit(0)
