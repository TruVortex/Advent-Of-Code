from queue import Queue

input = open('input', 'r')
lookup, adj = {'start': 0, 'end': 1}, {'start': [], 'end': []}
for line in input:
    u, v = line.strip().split('-')
    if u not in lookup:
        lookup[u] = len(lookup)
        adj[u] = []
    if v not in lookup:
        lookup[v] = len(lookup)
        adj[v] = []
    adj[u].append(v)
    adj[v].append(u)
q = Queue()
q.put(['start', [True, True] + [False] * 50, False, []])
ans = set()
while not q.empty():
    cur = q.get()
    for v in adj[cur[0]]:
        if v == 'end':
            ans.add(' '.join(cur[3]))
            continue
        idx = lookup[v]
        if v.isupper() or not cur[1][idx]:
            q.put([v, cur[1][:idx] + [True] + cur[1][idx + 1:], cur[2], cur[3] + [v]])
        if v != 'start' and not cur[2]:
            q.put([v, cur[1], True, cur[3] + [v]])
print(len(ans))
