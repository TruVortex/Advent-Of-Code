input = open('input', 'r')
tree = {'/': [None, 0, [], {}]}
ans, idx, cur, line = 0, 0, '', input.readline()
while line != '':
    if line[2] == 'c':
        if line[5] == '.':
            cur = tree[cur][0]
        elif line[5] == '/':
            cur = '/'
        else:
            cur = tree[cur][3][line.strip().split()[2]]
        line = input.readline()
    else:
        line = input.readline()
        while line != '' and line[0] != '$':
            if line[0].isdigit():
                tree[cur][1] += int(line.split()[0])
            else:
                tree[cur][2].append(line.strip().split()[1] + str(idx))
                tree[cur][3][line.strip().split()[1]] = line.strip().split()[1] + str(idx)
                tree[line.strip().split()[1] + str(idx)] = [cur, 0, [], {}]
            line = input.readline()
            idx += 1


def dfs(v):
    global tree, ans
    for u in tree[v][2]:
        tree[v][1] += dfs(u)
    if tree[v][1] <= 100000:
        ans += tree[v][1]
    return tree[v][1]


dfs('/')
print(ans)
