input = open('input', 'r')
depths = list(map(int, input.read().split()))
ans = 0
for i in range(3, len(depths)):
    if depths[i] > depths[i - 3]:
        ans += 1
print(ans)
