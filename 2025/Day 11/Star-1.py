connections, q, ans = {line[:3]: line[5:].split() for line in open('input', 'r')}, ['you'], 0
while q:
    cur = q.pop()
    for connection in connections[cur]:
        if connection == 'out':
            ans += 1
        else:
            q.append(connection)
print(ans)
