time, distance = open('input', 'r').readlines()
time = list(map(int, time[5:].split()))
distance = list(map(int, distance[9:].split()))
total = 1
for (race, record) in zip(time, distance):
    cur = 0
    for i in range(1, race):
        if i * (race - i) > record:
            cur += 1
    total *= max(cur, 1)
print(total)
