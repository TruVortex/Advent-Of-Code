from string import ascii_lowercase, ascii_uppercase

input = open('input', 'r')
lines = input.read().strip().split()
ans = 0
for i in range(0, len(lines), 3):
    for c in ascii_lowercase:
        if c in lines[i] and c in lines[i + 1] and c in lines[i + 2]:
            ans += ord(c) - ord('a') + 1
            break
    for c in ascii_uppercase:
        if c in lines[i] and c in lines[i + 1] and c in lines[i + 2]:
            ans += ord(c) - ord('A') + 27
            break
print(ans)
