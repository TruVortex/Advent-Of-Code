ticker = {'children': '3', 'cats': '7', 'samoyeds': '2', 'pomeranians': '3', 'akitas': '0', 'vizslas': '0', 'goldfish': '5', 'trees': '3', 'cars': '2', 'perfumes': '1'}
for i, line in enumerate(open('input', 'r')):
    flag = True
    for value in line[line.find(':') + 1:].strip().split(', '):
        flag &= ticker[value.split(':')[0]] == value.split(' ')[1]
    if flag:
        print(i + 1)
