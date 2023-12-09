cnt = 0
for string in open('input', 'r'):
    cnt += any(string.count(string[i - 1:i + 1]) >= 2 for i in range(1, len(string))) and any(string[i - 2] == string[i] for i in range(2, len(string)))
print(cnt)
