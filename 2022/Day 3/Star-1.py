from string import ascii_lowercase, ascii_uppercase

input = open('input', 'r')
ans = 0
for line in input:
    first, second = line[:len(line) // 2], line[len(line) // 2:]
    for c in ascii_lowercase:
        if c in first and c in second:
            ans += ord(c) - ord('a') + 1
            break
    for c in ascii_uppercase:
        if c in first and c in second:
            ans += ord(c) - ord('A') + 27
            break
print(ans)
