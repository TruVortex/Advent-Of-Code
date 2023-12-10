import re

seconds, ans = 2503, 0
reindeers = [[0, 0] + list(map(int, re.findall(r'\d+', line))) for line in open('input', 'r')]
for second in range(seconds):
    for reindeer in reindeers:
        if second % (reindeer[3] + reindeer[4]) < reindeer[3]:
            reindeer[1] += reindeer[2]
    for reindeer in reindeers:
        if reindeer[1] == max(deer[1] for deer in reindeers):
            reindeer[0] += 1
print(max(deer[0] for deer in reindeers))
