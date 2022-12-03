from string import ascii_letters

input = open('input', 'r')
ans = 0
for line in input:
    for c in ascii_letters:
        if c in line[:len(line) // 2] and c in line[len(line) // 2:]:
            if c.isupper():
                ans += ord(c) - ord('A') + 27
            else:
                ans += ord(c) - ord('a') + 1
            break
print(ans)
