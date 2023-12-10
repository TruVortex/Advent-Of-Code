import re

seconds, ans = 2503, 0
for line in open('input', 'r'):
    speed, time, rest = map(int, re.findall(r'\d+', line))
    ans = max(ans, speed * (time * (seconds // (time + rest)) + min(time, seconds % (time + rest))))
print(ans)
