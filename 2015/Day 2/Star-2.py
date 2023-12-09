summate = 0
for dimensions in open('input', 'r'):
    dimension = list(map(int, dimensions.split('x')))
    summate += dimension[0] * dimension[1] * dimension[2] + 2 * min(dimension[0] + dimension[1], dimension[0] + dimension[2], dimension[1] + dimension[2])
print(summate)
