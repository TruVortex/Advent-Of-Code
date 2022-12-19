from math import ceil

input = open('input', 'r')


def dp(blueprint, maxx, seen, time, resources, bots):
    if not time:
        return resources[3]
    key = (time, *resources, *bots)
    if key in seen:
        return seen[key]
    cur = resources[3] + bots[3] * time
    for bot, recipe in enumerate(blueprint):
        if bot == 3 or bots[bot] < maxx[bot]:
            time_needed = 0
            for resource, amount in recipe:
                if not bots[resource]:
                    break
                time_needed = max(time_needed, ceil((amount - resources[resource]) / bots[resource]))
            else:
                time_remaining = time - time_needed - 1
                if time_remaining <= 0:
                    continue
                new_bots, new_resources = bots.copy(), [resources[i] + bots[i] * (time_needed + 1) for i in range(4)]
                new_bots[bot] += 1
                for resource, amount in recipe:
                    new_resources[resource] -= amount
                cur = max(cur, dp(blueprint, maxx, seen, time_remaining, new_resources, new_bots))
    seen[key] = cur
    return cur


ans = 0
for idx, line in enumerate(input, 1):
    line = line.split()
    maxx = (max(int(line[6]), int(line[12]), int(line[18]), int(line[27])), int(line[21]), int(line[30]))
    blueprint = ([(0, int(line[6]))], [(0, int(line[12]))], [(0, int(line[18])), (1, int(line[21]))], [(0, int(line[27])), (2, int(line[30]))])
    ans += idx * dp(blueprint, maxx, {}, 24, [0] * 4, [1] + [0] * 3)
print(ans)
