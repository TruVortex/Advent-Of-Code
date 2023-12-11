containers = open('input', 'r').readlines()
cnt, cur = 0, len(containers)
for mask in range(1 << len(containers)):
    summate = set_bits = 0
    for i in range(len(containers)):
        if mask & (1 << i):
            summate += int(containers[i])
            set_bits += 1
    if summate == 150:
        if set_bits < cur:
            cnt = 0
            cur = set_bits
        cnt += set_bits == cur
print(cnt)
