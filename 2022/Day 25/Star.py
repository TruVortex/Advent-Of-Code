add, ans = 0, ''
for line in open('input', 'r').read().splitlines():
    for idx, num in enumerate(line[::-1]):
        add += ('=-012'.find(num) - 2) * 5 ** idx
while add:
    add, mod = divmod(add, 5)
    ans = '012=-'[mod] + ans
    if mod >= 3:
        add += 1
print(ans)
