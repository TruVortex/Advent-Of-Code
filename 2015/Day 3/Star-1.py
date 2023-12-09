cur = (0, 0)
distinct, delta = {(0, 0)}, {'<': (0, -1), '>': (0, 1), 'v': (-1, 0), '^': (1, 0)}
for move in open('input', 'r').readline():
    cur = tuple(map(sum, zip(cur, delta[move])))
    distinct.add(cur)
print(len(distinct))
