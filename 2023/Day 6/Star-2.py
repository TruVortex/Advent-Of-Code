import re

time, distance = open('input', 'r').readlines()
time = int(re.sub('\s', '', time[5:]))
distance = int(re.sub('\s', '', distance[9:]))
total = 0
for i in range(1, time):
    if i * (time - i) > distance:
        total += 1
print(total)
