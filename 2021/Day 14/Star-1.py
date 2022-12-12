from collections import defaultdict

input = open('input', 'r')
rules = defaultdict(str)
cur, insertions = input.read().split('\n\n')
for line in insertions.splitlines():
    insertion = line.split(' -> ')
    rules[insertion[0]] = insertion[1]
for i in range(10):
    new = cur[0]
    for j in range(1, len(cur)):
        new += rules[cur[j - 1] + cur[j]]
        new += cur[j]
    cur = new
freq = []
for i in range(26):
    freq.append(cur.count(chr(ord('A') + i)))
print(max(freq) - min([x for x in freq if x > 0]))
