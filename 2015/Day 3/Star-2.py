santa = robo = (0, 0)
route = open('input', 'r').readline()
distinct, delta = {(0, 0)}, {'<': (0, -1), '>': (0, 1), 'v': (-1, 0), '^': (1, 0)}
for i in range(0, len(route), 2):
    santa = tuple(map(sum, zip(santa, delta[route[i]])))
    robo = tuple(map(sum, zip(robo, delta[route[i + 1]])))
    distinct.add(santa)
    distinct.add(robo)
print(len(distinct))
