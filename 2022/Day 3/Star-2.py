from string import ascii_letters

input = open('input', 'r')
lines = input.read().strip().split()
ans = 0
for i in range(0, len(lines), 3):
    for c in ascii_letters:
        if c in lines[i] and c in lines[i + 1] and c in lines[i + 2]:
            if c.isupper():
                ans += ord(c) - ord('A') + 27
            else:
                ans += ord(c) - ord('a') + 1
            break
print(ans)
