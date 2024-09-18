keypad = (
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 0, 0, 0),
    (0, 0, 2, 3, 4, 0, 0),
    (0, 5, 6, 7, 8, 9, 0),
    (0, 0, 'A', 'B', 'C', 0, 0),
    (0, 0, 0, 'D', 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
)
delta = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
for line in open('input', 'r'):
    x = y = 3
    for char in line.strip():
        x += delta[char][0]
        y += delta[char][1]
        if keypad[y][x] == 0:
            x -= delta[char][0]
            y -= delta[char][1]
    print(keypad[y][x], end='')
