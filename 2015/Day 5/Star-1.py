import re

cnt = 0
for string in open('input', 'r'):
    cnt += len(re.split(r'[aeiou]', string)) > 3 and len(re.findall(r'(.)\1', string)) > 0 and all(pair not in string for pair in ['ab', 'cd', 'pq', 'xy'])
print(cnt)
