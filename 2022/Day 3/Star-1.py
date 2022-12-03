from string import ascii_letters

input = open('input', 'r')
ans = 0
for line in input:
    first, second = line[:len(line) // 2], line[len(line) // 2:]
    for c in ascii_letters:
        if c in first and c in second:
            if c.isupper():
                ans += ord(c) - ord('A') + 27
            else:
                ans += ord(c) - ord('a') + 1
            break
print(ans)
