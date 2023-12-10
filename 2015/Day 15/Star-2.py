import re


def combinations(idx, remaining, capacity, durability, flavour, texture, calories):
    global cookies
    if idx == len(cookies) - 1:
        if calories + remaining * cookies[idx][4] != 500:
            return 0
        return max(0, (capacity + remaining * cookies[idx][0])) * max(0, (durability + remaining * cookies[idx][1])) * max(0, (flavour + remaining * cookies[idx][2])) * max(0, (texture + remaining * cookies[idx][3]))
    return max(combinations(idx + 1, remaining - i, capacity + i * cookies[idx][0], durability + i * cookies[idx][1], flavour + i * cookies[idx][2], texture + i * cookies[idx][3], calories + i * cookies[idx][4]) for i in range(remaining + 1))


cookies = [list(map(int, re.findall(r'-?\d+', line))) for line in open('input', 'r')]
print(combinations(0, 100, 0, 0, 0, 0, 0))
