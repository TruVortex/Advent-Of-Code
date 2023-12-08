import re

min_x, max_x, min_y, max_y = map(int, re.findall(r'-?\d+', open('input', 'r').readline()))
ans = set()
for dy in range(min_y - 1, -min_y + 1):
    y = cnt = 0
    ddy = dy
    pos = []
    while y >= min_y:
        if y <= max_y:
            for dx in range(1, max_x + 1):
                x = 0
                ddx = dx
                for _ in range(cnt):
                    x += ddx
                    if ddx:
                        ddx -= 1
                if min_x <= x <= max_x:
                    ans.add((dy, dx))
        y += ddy
        ddy -= 1
        cnt += 1
    dy -= 1
print(len(ans))
