hands = []
cards = '23456789ABCDE'
for line in open('input', 'r'):
    hand, bid = line.split()
    hand = hand.replace('A', 'E')
    hand = hand.replace('K', 'D')
    hand = hand.replace('Q', 'C')
    hand = hand.replace('J', '1')
    hand = hand.replace('T', 'A')
    new = []
    for replace in cards:
        new_card = hand.replace('1', replace)
        distinct = {}
        for card in new_card:
            if card in distinct:
                distinct[card] += 1
            else:
                distinct[card] = 1
        power = len(set(new_card))
        if power == 1:
            new.append((7, hand, bid))
        elif power == 2:
            if 4 in distinct.values():
                new.append((6, hand, bid))
            else:
                new.append((5, hand, bid))
        elif power == 3:
            if 3 in distinct.values():
                new.append((4, hand, bid))
            else:
                new.append((3, hand, bid))
        elif power == 4:
            new.append((2, hand, bid))
        else:
            new.append((1, hand, bid))
    hands.append(sorted(new)[-1])
summate = 0
for rank, hand in enumerate(sorted(hands)):
    summate += (rank + 1) * int(hand[2])
    print(hand)
print(summate)
