import re
from collections import defaultdict
from itertools import permutations

adj = defaultdict(dict)
for line in open('input', 'r'):
    u, v, dist = re.match(r'(\w+) to (\w+) = (\d+)', line).groups()
    adj[u][v] = adj[v][u] = int(dist)
ans = 0
for permutation in list(permutations(adj)):
    ans = max(ans, sum(adj[permutation[i]][permutation[i - 1]] for i in range(1, len(permutation))))
print(ans)
