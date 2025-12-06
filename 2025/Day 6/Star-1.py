lines, total = [line.split() for line in open('input', 'r')], 0
for i in range(len(lines[0])):
    numbers = [line[i] for line in lines[:-1]]
    to_eval = numbers[0]
    for number in numbers[1:]:
        to_eval += lines[-1][i] + number
    total += eval(to_eval)
print(total)
