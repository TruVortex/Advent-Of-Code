input = open('input', 'r')
rope = [(0, 0) for i in range(10)]
pos = {(0, 0)}
for line in input:
    command = line.split()
    for i in range(int(command[1])):
        if command[0] == 'R':
            rope[0] = (rope[0][0] + 1, rope[0][1])
        elif command[0] == 'L':
            rope[0] = (rope[0][0] - 1, rope[0][1])
        elif command[0] == 'U':
            rope[0] = (rope[0][0], rope[0][1] + 1)
        else:
            rope[0] = (rope[0][0], rope[0][1] - 1)
        for j in range(9):
            if rope[j][0] - rope[j + 1][0] == 2 and rope[j][1] - rope[j + 1][1] == 2:
                rope[j + 1] = (rope[j][0] - 1, rope[j][1] - 1)
            elif rope[j][0] - rope[j + 1][0] == 2 and rope[j + 1][1] - rope[j][1] == 2:
                rope[j + 1] = (rope[j][0] - 1, rope[j][1] + 1)
            elif rope[j + 1][0] - rope[j][0] == 2 and rope[j][1] - rope[j + 1][1] == 2:
                rope[j + 1] = (rope[j][0] + 1, rope[j][1] - 1)
            elif rope[j + 1][0] - rope[j][0] == 2 and rope[j + 1][1] - rope[j][1] == 2:
                rope[j + 1] = (rope[j][0] + 1, rope[j][1] + 1)
            elif rope[j][0] - rope[j + 1][0] == 2:
                rope[j + 1] = (rope[j][0] - 1, rope[j][1])
            elif rope[j + 1][0] - rope[j][0] == 2:
                rope[j + 1] = (rope[j][0] + 1, rope[j][1])
            elif rope[j][1] - rope[j + 1][1] == 2:
                rope[j + 1] = (rope[j][0], rope[j][1] - 1)
            elif rope[j + 1][1] - rope[j][1] == 2:
                rope[j + 1] = (rope[j][0], rope[j][1] + 1)
        pos.add(rope[9])
print(len(pos))
