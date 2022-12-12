input = open('input', 'r')
cur, rules = {}, {}
word, insertions = input.read().split('\n\n')
for i in range(1, len(word)):
    if (word[i - 1] + word[i]) not in cur:
        cur[word[i - 1] + word[i]] = 0
    cur[word[i - 1] + word[i]] += 1
for line in insertions.splitlines():
    insertion = line.split(' -> ')
    rules[insertion[0]] = insertion[1]
for i in range(40):
    new = {}
    for key, value in cur.items():
        if key in rules:
            if (key[0] + rules[key]) not in new:
                new[key[0] + rules[key]] = 0
            new[key[0] + rules[key]] += value
            if (rules[key] + key[1]) not in new:
                new[rules[key] + key[1]] = 0
            new[rules[key] + key[1]] += value
        else:
            if key not in new:
                new[key] = 0
            new[key] += value
    cur = new
first, freq = True, [0] * 26
for key, value in cur.items():
    if first:
        first = False
        freq[ord(key[0]) - ord('A')] += value
    freq[ord(key[1]) - ord('A')] += value
print(max(freq) - min([x for x in freq if x > 0]))
