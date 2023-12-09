from itertools import groupby

sequence = '1113122113'
for i in range(50):
    sequence = ''.join(str(len(list(g))) + k for k, g in groupby(sequence))
print(len(sequence))
