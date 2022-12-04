input = open('input', 'r')
ans = 0
for line in input:
    digits = line.split('|')[1].split()
    for digit in digits:
        if 2 <= len(digit) <= 4 or len(digit) == 7:
            ans += 1
print(ans)
