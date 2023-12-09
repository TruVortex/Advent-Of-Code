def extrapolate(values):
    if all(value == 0 for value in values):
        return 0
    return values[0] - extrapolate([values[i] - values[i - 1] for i in range(1, len(values))])


summate = 0
for line in open('input', 'r'):
    summate += extrapolate(list(map(int, line.split())))
print(summate)
