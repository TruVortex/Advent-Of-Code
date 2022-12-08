from math import prod

grid = open('input', 'r').read().split()
ans, moves = 0, ((-1, 0), (1, 0), (0, -1), (0, 1))
for r in range(len(grid)):
    for c in range(len(grid[0])):
        lengths = []
        for move in moves:
            tempR, tempC, length = r, c, 0
            while True:
                tempR += move[0]
                tempC += move[1]
                length += 1
                if not (0 <= tempR < len(grid) and 0 <= tempC < len(grid[0])):
                    length -= 1
                    break
                if grid[tempR][tempC] >= grid[r][c]:
                    break
            lengths.append(length)
        ans = max(ans, prod(lengths))
print(ans)
