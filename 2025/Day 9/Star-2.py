def contains(px, py, x1, y1, x2, y2):
    return min(x1, x2) < px < max(x1, x2) and min(y1, y2) < py < max(y1, y2)


def sgn(n):
    return (n > 0) - (n < 0)


tiles, ans = [tuple(map(int, line.split(','))) for line in open('input', 'r')], 0
for i, tile in enumerate(tiles):
    for j in range(i + 1, len(tiles)):
        cnt, mx, my, dx, dy = 0, (tile[0] + tiles[j][0]) // 2 + 0.5, (tile[1] + tiles[j][1]) // 2 + 0.5, 0.5 * sgn(tiles[j][0] - tile[0]), 0.5 * sgn(tiles[j][1] - tile[1])
        for k in range(len(tiles)):
            (ex1, ex2), (ey1, ey2) = sorted((tiles[k - 1][0], tiles[k][0])), sorted((tiles[k - 1][1], tiles[k][1]))
            if (contains(tiles[k - 1][0], tiles[k][1], *tile, *tiles[j]) or
                contains(tiles[k][0], tiles[k - 1][1], *tile, *tiles[j]) or
                ex1 == ex2 and min(tile[0], tiles[j][0]) < ex1 < max(tile[0], tiles[j][0]) and ey1 <= min(tile[1], tiles[j][1]) and ey2 >= max(tile[1], tiles[j][1]) or
                ey1 == ey2 and min(tile[1], tiles[j][1]) < ey1 < max(tile[1], tiles[j][1]) and ex1 <= min(tile[0], tiles[j][0]) and ex2 >= max(tile[0], tiles[j][0])):
                break
            cnt += ex1 == ex2 and ex1 > mx and ey1 < my <= ey2
        else:
            if cnt % 2:
                ans = max(ans, (abs(tile[0] - tiles[j][0]) + 1) * (abs(tile[1] - tiles[j][1]) + 1))
print(ans)
