import re

min_x, max_x, min_y, max_y = map(int, re.findall(r'-?\d+', open('input', 'r').readline()))
dy = -min_y
while True:
    y = cnt = 0
    ddy = dy
    pos = []
    while y >= min_y:
        if y <= max_y:
            for ddx in range(1, max_x):
                x = 0
                for _ in range(cnt):
                    x += ddx
                    if ddx:
                        ddx -= 1
                if min_x <= x <= max_x:
                    print(dy * (dy + 1) // 2)
                    exit(0)
        y += ddy
        ddy -= 1
        cnt += 1
    dy -= 1
