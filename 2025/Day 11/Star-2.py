from collections import defaultdict

connections, q, dp = {line[:3]: line[5:].split() for line in open('input', 'r')}, ['out'], defaultdict(int, [(('out', False, False), 1)])
while q:
    to_pop, cur = [], q.pop()
    for key, value in connections.items():
        if cur in value:
            if key == 'dac':
                dp[(key, True, False)] += dp[(cur, False, False)]
                dp[(key, True, True)] += dp[(cur, False, True)]
            elif key == 'fft':
                dp[(key, False, True)] += dp[(cur, False, False)]
                dp[(key, True, True)] += dp[(cur, True, False)]
            dp[(key, False, False)] += dp[(cur, False, False)]
            dp[(key, False, True)] += dp[(cur, False, True)]
            dp[(key, True, False)] += dp[(cur, True, False)]
            dp[(key, True, True)] += dp[(cur, True, True)]
            value.remove(cur)
            if not value:
                to_pop.append(key)
                q.append(key)
    for key in to_pop:
        connections.pop(key)
print(dp[('svr', True, True)])
