input = open('input', 'r')
crabs = list(map(int, input.readline().split(',')))
ans = 1e9
for i in range(max(crabs)):
    cur = 0
    for crab in crabs:
        cur += abs(crab - i)
    ans = min(ans, cur)
print(ans)
