import re

cnt = 0
for line in open('input', 'r'):
    springs, records = line.split()
    unknown = []
    for i, ch in enumerate(springs):
        if ch == '?':
            unknown.append(i)
    for mask in range(1 << len(unknown)):
        new = list(springs)
        for i in range(len(unknown)):
            new[unknown[i]] = '#' if mask & (1 << i) else '.'
        cnt += records == ','.join([str(len(match)) for match in re.findall(r'#+', ''.join(new))])
print(cnt)
