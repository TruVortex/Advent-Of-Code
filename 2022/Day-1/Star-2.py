input = open('input', 'r')
line = input.readline()
cur = 0
arr = []
while line != 'x':
    if line == '\n':
        arr.append(cur)
        cur = 0
    else:
        cur += int(line.strip())
    line = input.readline()
arr.append(cur)
arr.sort()
print(arr[-1] + arr[-2] + arr[-3])
