from queue import Queue

flipflop, conjunction, low, high = {}, {}, 0, 0
for line in open('input', 'r'):
    if line[0] == '&':
        conjunction[line[1:line.find(' ')]] = [[], line.strip()[line.find('->') + 3:].split(', ')]
    else:
        flipflop[line[1:line.find(' ')]] = [False, line.strip()[line.find('->') + 3:].split(', ')]
for source, destinations in flipflop.items():
    for destination in destinations[1]:
        if destination in conjunction:
            conjunction[destination][0].append(source)
for source, destinations in conjunction.items():
    for destination in destinations[1]:
        if destination in conjunction:
            conjunction[destination][0].append(source)


def check(sources):
    global flipflop, conjunction
    for source_check in sources:
        if source_check in flipflop:
            if not flipflop[source_check][0]:
                return True
        elif not check(conjunction[source_check][0]):
            return True
    return False


for _ in range(1000):
    low += 1
    q = Queue()
    for destination in flipflop['roadcaster'][1]:
        q.put((False, destination))
    while not q.empty():
        cur = q.get()
        low += not cur[0]
        high += cur[0]
        if cur[1] in flipflop:
            if not cur[0]:
                send = flipflop[cur[1]][0] = flipflop[cur[1]][0] ^ True
                for destination in flipflop[cur[1]][1]:
                    q.put((send, destination))
        elif cur[1] in conjunction:
            send = check(conjunction[cur[1]][0])
            for destination in conjunction[cur[1]][1]:
                q.put((send, destination))
print(low * high)
