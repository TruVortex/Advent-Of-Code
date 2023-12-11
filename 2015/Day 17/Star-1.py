containers = open('input', 'r').readlines()
cnt = 0
for mask in range(1 << len(containers)):
    summate = 0
    for i in range(len(containers)):
        if mask & (1 << i):
            summate += int(containers[i])
    cnt += summate == 150
print(cnt)
