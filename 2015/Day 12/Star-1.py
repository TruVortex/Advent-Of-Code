import re

print(sum(map(int, re.findall(r'(-?[0-9]+)', open('input', 'r').read()))))
