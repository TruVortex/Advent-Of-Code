fish = list(map(int, open('input', 'r').readline().strip().split(',')))
for i in range(80):
    cur = len(fish)
    for j in range(cur):
        fish[j] -= 1
        if fish[j] < 0:
            fish[j] = 6
            fish.append(8)
print(len(fish))
