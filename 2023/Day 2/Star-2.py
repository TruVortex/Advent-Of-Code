summate = 0
for line in open('input', 'r'):
    subsets = line[line.index(':') + 1:].strip().replace(';', ',').split(', ')
    seen = {'red': 1, 'green': 1, 'blue': 1}
    for colour in subsets:
        if colour.endswith('red'):
            seen['red'] = max(seen['red'], int(colour[:-4]))
        elif colour.endswith('green'):
            seen['green'] = max(seen['green'], int(colour[:-6]))
        else:
            seen['blue'] = max(seen['blue'], int(colour[:-5]))
    summate += seen['red'] * seen['green'] * seen['blue']
print(summate)
