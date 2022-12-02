input = open('input', 'r')
ans = 0
for line in input:
    moves = line.split()
    if moves[1] == 'X':
        ans += 1
    elif moves[1] == 'Y':
        ans += 2
    else:
        ans += 3
    if (moves[0] == 'A' and moves[1] == 'Y') or (moves[0] == 'B' and moves[1] == 'Z') or (moves[0] == 'C' and moves[
        1] == 'X'):
        ans += 6
    elif (moves[0] == 'A' and moves[1] == 'X') or (moves[0] == 'B' and moves[1] == 'Y') or (moves[0] == 'C' and moves[
        1] == 'Z'):
        ans += 3
print(ans)
