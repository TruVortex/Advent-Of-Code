input = open('input', 'r')
head, tail = (0, 0), (0, 0)
pos = {(0, 0)}
for line in input:
    command = line.split()
    for i in range(int(command[1])):
        if command[0] == 'R':
            head = (head[0] + 1, head[1])
        elif command[0] == 'L':
            head = (head[0] - 1, head[1])
        elif command[0] == 'U':
            head = (head[0], head[1] + 1)
        else:
            head = (head[0], head[1] - 1)
        if head[0] - tail[0] == 2:
            tail = (head[0] - 1, head[1])
        elif tail[0] - head[0] == 2:
            tail = (head[0] + 1, head[1])
        elif head[1] - tail[1] == 2:
            tail = (head[0], head[1] - 1)
        elif tail[1] - head[1] == 2:
            tail = (head[0], head[1] + 1)
        pos.add(tail)
print(len(pos))
