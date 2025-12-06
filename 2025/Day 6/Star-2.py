lines = open('input', 'r').read().split('\n')
total, indices, nsymbols, idx = 0, [], lines[-1], -1
while '+' in nsymbols or '*' in nsymbols:
    nidx = min(nsymbols.find('+') if nsymbols.find('+') >= 0 else float('inf'),
               nsymbols.find('*') if nsymbols.find('*') >= 0 else float('inf'))
    nsymbols = nsymbols[nidx + 1:]
    idx += nidx + 1
    indices.append(idx)
indices.append(len(lines[0]) + 1)
symbols = lines[-1].split()
for i in range(len(symbols)):
    numbers = [''.join(line[j] for line in lines[:-1]) for j in range(indices[i], indices[i + 1] - 1)]
    to_eval = numbers[0]
    for number in numbers[1:]:
        to_eval += symbols[i] + number
    total += eval(to_eval)
print(total)
