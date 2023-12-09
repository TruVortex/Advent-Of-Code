import re
from collections import defaultdict
from itertools import permutations

seats = defaultdict(dict)
for line in open('input', 'r'):
    person_a, happiness, person_b = re.match('(\w+) would gain (-?\d+) happiness units by sitting next to (\w+)', line.replace('lose ', 'gain -')).groups()
    seats[person_a][person_b] = int(happiness)
ans = 0
for permutation in permutations(list(seats.keys())[1:]):
    permutation = [list(seats.keys())[0]] + list(permutation)
    ans = max(ans, sum(seats[permutation[i]][permutation[i - 1]] + seats[permutation[i]][permutation[i + 1 - len(permutation)]] for i in range(len(permutation))))
print(ans)
