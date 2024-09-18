for line in open('input', 'r'):
    x = y = 1
    for char in line:
        if char == 'U':
            y = max(0, y - 1)
        elif char == 'D':
            y = min(2, y + 1)
        elif char == 'L':
            x = max(0, x - 1)
        else:
            x = min(2, x + 1)
    print(((1, 2, 3), (4, 5, 6), (7, 8, 9))[y][x], end='')
