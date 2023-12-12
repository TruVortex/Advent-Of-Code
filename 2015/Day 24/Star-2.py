packages = list(map(int, open('input', 'r').readlines()))
dp, ways = [set() for _ in range(sum(packages) // 3 + 1)], []
dp[0].add(())
for i in range(1, sum(packages) // 4 + 1):
    min_length = len(packages)
    for package in packages:
        if i - package >= 0:
            for way in dp[i - package]:
                if package not in way:
                    dp[i].add(tuple(sorted(list(way) + [package])))
                    min_length = min(min_length, len(way) + 1)
    remove = []
    for way in dp[i]:
        if len(way) > min_length + 1:
            remove.append(way)
    for element in remove:
        dp[i].remove(element)
for way in dp[sum(packages) // 4]:
    cnt, qe, mask = 0, 1, 0
    for i, package in enumerate(packages):
        if package in way:
            cnt += 1
            qe *= package
            mask |= 1 << i
    ways.append((cnt, qe, mask))
for way_1 in sorted(ways):
    for way_2 in ways:
        for way_3 in ways:
            if way_1[2] & way_2[2] & way_3[2] == 0:
                print(way_1[1])
                exit(0)
