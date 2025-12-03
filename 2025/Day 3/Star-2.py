total = 0
for line in open('input', 'r'):
    line = line.strip()
    dp = [[0] * 13 for i in range(len(line) + 1)]
    for i in range(1, len(dp)):
        num = int(line[i - 1])
        dp[i][1] = max(dp[i - 1][1], num)
        for j in range(2, min(i + 1, 13)):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] * 10 + num)
    total += dp[-1][12]
print(total)
