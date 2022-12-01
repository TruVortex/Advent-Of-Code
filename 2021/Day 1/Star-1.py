input = open('input', 'r')
depths = list(map(int, input.read().split()))
ans = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        ans += 1
print(ans)
