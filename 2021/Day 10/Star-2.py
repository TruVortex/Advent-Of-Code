input = open('input', 'r')
ans = []
for line in input:
    line = line.strip()
    leave = False
    expected = []
    for char in line:
        if char in '([{<':
            expected.append({'(': ')', '[': ']', '{': '}', '<': '>'}[char])
        else:
            if char == expected[-1]:
                expected.pop()
            else:
                leave = True
                break
    if not leave:
        cur = 0
        for char in reversed(expected):
            cur *= 5
            cur += {')': 1, ']': 2, '}': 3, '>': 4}[char]
        ans.append(cur)
print(sorted(ans)[len(ans) // 2])
