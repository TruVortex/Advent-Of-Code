input = open('input', 'r')
crates = [[] for i in range(100)]
length: int
while (line := input.readline())[1] != '1':
    length = len(line) // 4
    for i in range(0, len(line), 4):
        if line[i + 1] != ' ':
            crates[i // 4].insert(0, line[i + 1])
input.readline()
while (line := input.readline()) != '':
    command = line.split()
    for i in range(int(command[1])):
        crates[int(command[5]) - 1].append(crates[int(command[3]) - 1][len(crates[int(command[3]) - 1]) - int(command[1]) + i])
    for i in range(int(command[1])):
        crates[int(command[3]) - 1].pop()
    print(crates)
for i in range(length):
    print(crates[i][-1], end='')
