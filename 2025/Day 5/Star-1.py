ranges, ids = open('input', 'r').read().split('\n\n')
cnt = 0
for available in ids.split('\n'):
    for fresh in ranges.split('\n'):
        l, r = fresh.split('-')
        if int(l) <= int(available) <= int(r):
            cnt += 1
            break
print(cnt)
