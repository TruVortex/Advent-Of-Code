print(sum(len(rf'{line.strip()}') - len(eval(line)) for line in open('input', 'r')))
