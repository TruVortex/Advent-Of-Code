grid = open('input', 'r').read().split()
ans, moves = 0, ((-1, 0), (1, 0), (0, -1), (0, 1))
for r in range(len(grid)):
    for c in range(len(grid[0])):
        for move in moves:
            tempR, tempC, valid = r, c, True
            while True:
                tempR += move[0]
                tempC += move[1]
                if not (0 <= tempR < len(grid) and 0 <= tempC < len(grid[0])):
                    break
                if grid[tempR][tempC] >= grid[r][c]:
                    valid = False
                    break
            if valid:
                ans += 1
                break
print(ans)
