from collections import defaultdict

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
    total += valid * int(page_numbers[len(page_numbers) // 2])
print(total)
