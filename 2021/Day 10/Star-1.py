input = open('input', 'r')
ans = 0
for line in input:
    line = line.strip()
    expected = []
    for char in line:
        if char in '([{<':
            expected.append({'(': ')', '[': ']', '{': '}', '<': '>'}[char])
        else:
            if expected and char == expected[-1]:
                expected.pop()
            else:
                ans += {')': 3, ']': 57, '}': 1197, '>': 25137}[char]
                break
print(ans)
