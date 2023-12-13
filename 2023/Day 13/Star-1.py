summate, patterns = 0, [pattern.split() for pattern in open('input', 'r').read().split('\n\n')]
for pattern in patterns:
    for i in range(1, len(pattern)):
        flag = True
        for j in range(min(i, len(pattern) - i)):
            flag &= pattern[i - j - 1] == pattern[i + j]
        if flag:
            summate += 100 * i
    for i in range(1, len(pattern[0])):
        flag = True
        for j in range(min(i, len(pattern[0]) - i)):
            for k in range(len(pattern)):
                flag &= pattern[k][i - j - 1] == pattern[k][i + j]
        if flag:
            summate += i
print(summate)
