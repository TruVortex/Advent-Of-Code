from collections import defaultdict
from functools import cmp_to_key


def cmp(a, b):
    global impossible
    if a in impossible[b]:
        return -1
    return 1


rules, pages = open('input', 'r').read().split('\n\n')
total, impossible = 0, defaultdict(set)
for rule in rules.split():
    x, y = rule.split('|')
    impossible[x].add(y)
for page in pages.split():
    page_numbers = page.split(',')
    valid = True
    for i in range(len(page_numbers)):
        for j in range(i):
            if page_numbers[j] in impossible[page_numbers[i]]:
                valid = False
    if not valid:
        total += int(sorted(page_numbers, key=cmp_to_key(cmp))[len(page_numbers) // 2])
print(total)
