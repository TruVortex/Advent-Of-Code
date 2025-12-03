total = 0
for line in open('input', 'r'):
    line = line.strip()
    total += max(max(list(map(int, list(line[:i])))) * 10 + max(list(map(int, list(line[i:])))) for i in range(1, len(line)))
print(total)
