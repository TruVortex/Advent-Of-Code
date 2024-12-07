def evaluate(cur, numbers):
    if not numbers:
        return [cur]
    return evaluate(cur + numbers[0], numbers[1:]) + evaluate(cur * numbers[0], numbers[1:]) + evaluate(int(str(cur) + str(numbers[0])), numbers[1:])


total = 0
for line in open('input', 'r'):
    value, numbers = line.split(': ')
    value, numbers = int(value), list(map(int, numbers.split()))
    if any(number == value for number in evaluate(numbers[0], numbers[1:])):
        total += value
print(total)
