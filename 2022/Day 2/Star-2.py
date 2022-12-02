input = open('input', 'r')
ans = 0
for line in input:
    moves = line.split()
    move: str
    if moves[1] == 'X':
        move = 'ABC'[('ABC'.find(moves[0]) + 2) % 3]
    elif moves[1] == 'Y':
        ans += 3
        move = moves[0]
    else:
        ans += 6
        move = 'ABC'[('ABC'.find(moves[0]) + 1) % 3]
    if move == 'A':
        ans += 1
    elif move == 'B':
        ans += 2
    else:
        ans += 3
print(ans)
