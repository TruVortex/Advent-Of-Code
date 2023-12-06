summate = 0
cnt = [1] * (len(open('input', 'r').readlines()) + 1)
for card, line in enumerate(open('input', 'r')):
    numbers = line[line.find(':') + 1:].split(' | ')
    winning, owned = list(map(int, numbers[0].split())), list(map(int, numbers[1].split()))
    cur = 1
    for num in winning:
        if num in owned:
            cur += 1
    for i in range(1, cur):
        if card + i < len(cnt):
            cnt[card + i] += cnt[card]
    summate += cnt[card]
print(summate)
