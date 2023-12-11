items = (((8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)), ((0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)), ((0, 0, 0), (0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)))
boss = None
ans = 999
for weapon in items[0]:
    for armour in items[1]:
        for i in range(len(items[2])):
            for j in range(i + 1, len(items[2])):
                ring_1, ring_2 = items[2][i], items[2][j]
                stats, temp, turn = [100, weapon[1] + armour[1] + ring_1[1] + ring_2[1], weapon[2] + armour[2] + ring_1[2] + ring_2[2]], list(boss), 1
                while stats[0] > 0 and temp[0] > 0:
                    if turn % 2:
                        temp[0] -= max(1, stats[1] - temp[2])
                    else:
                        stats[0] -= max(1, temp[1] - stats[2])
                    turn += 1
                if stats[0] > 0:
                    ans = min(ans, weapon[0] + armour[0] + ring_1[0] + ring_2[0])
print(ans)
