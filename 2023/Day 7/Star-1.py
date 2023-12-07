hands = []
for line in open('input', 'r'):
    hand, bid = line.split()
    hand = hand.replace('A', 'E')
    hand = hand.replace('K', 'D')
    hand = hand.replace('Q', 'C')
    hand = hand.replace('J', 'B')
    hand = hand.replace('T', 'A')
    distinct = {}
    for card in hand:
        if card in distinct:
            distinct[card] += 1
        else:
            distinct[card] = 1
    power = len(set(hand))
    if power == 1:
        hands.append((7, hand, bid))
    elif power == 2:
        if 4 in distinct.values():
            hands.append((6, hand, bid))
        else:
            hands.append((5, hand, bid))
    elif power == 3:
        if 3 in distinct.values():
            hands.append((4, hand, bid))
        else:
            hands.append((3, hand, bid))
    elif power == 4:
        hands.append((2, hand, bid))
    else:
        hands.append((1, hand, bid))
summate = 0
for rank, hand in enumerate(sorted(hands)):
    summate += (rank + 1) * int(hand[2])
print(summate)
