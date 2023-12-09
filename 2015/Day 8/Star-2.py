print(sum(2 + line.count('\\') + line.count('"') for line in open('input', 'r')))
