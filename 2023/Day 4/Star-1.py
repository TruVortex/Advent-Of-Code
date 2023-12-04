from math import floor

summate = 0
for line in open('input', 'r'):
    numbers = line[line.find(':') + 1:].split(' | ')
    winning, owned = list(map(int, numbers[0].split())), list(map(int, numbers[1].split()))
    cur = 0.5
    for num in winning:
        if num in owned:
            cur *= 2
    summate += floor(cur)
print(summate)
