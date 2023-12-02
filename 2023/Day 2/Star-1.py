summate = 0
for i, line in enumerate(open('input', 'r')):
    subsets = line[line.index(':') + 1:].strip().replace(';', ',').split(', ')
    seen = {'red': 0, 'green': 0, 'blue': 0}
    for colour in subsets:
        if colour.endswith('red'):
            seen['red'] = max(seen['red'], int(colour[:-4]))
        elif colour.endswith('green'):
            seen['green'] = max(seen['green'], int(colour[:-6]))
        else:
            seen['blue'] = max(seen['blue'], int(colour[:-5]))
    if seen['red'] <= 12 and seen['green'] <= 13 and seen['blue'] <= 14:
        summate += i + 1
print(summate)
