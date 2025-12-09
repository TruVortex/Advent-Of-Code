tiles, ans = [tuple(map(int, line.split(','))) for line in open('input', 'r')], 0
for i, tile in enumerate(tiles):
    for j in range(i + 1, len(tiles)):
        ans = max(ans, (abs(tile[0] - tiles[j][0]) + 1) * (abs(tile[1] - tiles[j][1]) + 1))
print(ans)
