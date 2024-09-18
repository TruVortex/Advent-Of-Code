ans = 0
for line in open('input', 'r'):
    lengths = sorted(list(map(int, line.split())))
    ans += (lengths[0] + lengths[1] > lengths[2])
print(ans)
