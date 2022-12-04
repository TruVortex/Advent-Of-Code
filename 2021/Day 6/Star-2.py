input = open('input', 'r')
line = input.readline()
fish = [line.count(str(i)) for i in range(9)]
for i in range(256):
    fish[7] += fish[0]
    fish = fish[1:] + fish[:1]
print(sum(fish))
