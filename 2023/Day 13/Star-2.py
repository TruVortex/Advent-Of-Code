summate, patterns = 0, [pattern.split() for pattern in open('input', 'r').read().split('\n\n')]
for pattern in patterns:
    for i in range(1, len(pattern)):
        cnt = 0
        for j in range(min(i, len(pattern) - i)):
            for k in range(len(pattern[0])):
                cnt += pattern[i - j - 1][k] != pattern[i + j][k]
        if cnt == 1:
            summate += 100 * i
    for i in range(1, len(pattern[0])):
        cnt = 0
        for j in range(min(i, len(pattern[0]) - i)):
            for k in range(len(pattern)):
                cnt += pattern[k][i - j - 1] != pattern[k][i + j]
        if cnt == 1:
            summate += i
print(summate)
