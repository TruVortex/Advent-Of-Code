import re

lights = [[0] * 1000 for i in range(1000)]
for line in open('input', 'r'):
    nums = list(map(int, re.findall(r'[0-9]+', line)))
    for y in range(nums[1], nums[3] + 1):
        for x in range(nums[0], nums[2] + 1):
            if line[1] == 'o':
                lights[y][x] += 2
            else:
                lights[y][x] += 1 if line[6] == 'n' else -1
                if lights[y][x] < 0:
                    lights[y][x] = 0
print(sum(map(sum, lights)))
