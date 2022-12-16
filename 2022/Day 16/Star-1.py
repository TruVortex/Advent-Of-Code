input = open('input', 'r')
idx = 0
lookup, flow, adj, memoize = {}, [], [], {}
for line in input:
    expanded = line.split()
    lookup[expanded[1]] = idx
    flow.append(int(expanded[4][5:-1]))
    adj.append(''.join(expanded[9:]).split(','))
    idx += 1
for i in range(len(adj)):
    for j, element in enumerate(adj[i]):
        adj[i][j] = lookup[element]


def dp(node, mask, time):
    global flow, adj, memoize
    if time == 0:
        return 0
    if (node, mask, time) in memoize:
        return memoize[(node, mask, time)]
    ans = 0
    if mask & (1 << node) == 0 and flow[node] > 0:
        ans = max(ans, dp(node, mask | (1 << node), time - 1) + (time - 1) * flow[node])
    for v in adj[node]:
        ans = max(ans, dp(v, mask, time - 1))
    memoize[(node, mask, time)] = ans
    return ans


print(dp(lookup['AA'], 0, 30))
