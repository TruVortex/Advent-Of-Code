from functools import cmp_to_key

input = open('input', 'r')
ans = 0
for line in input:
    decode, digits, display, = list(map(set, line.split('|')[0].split())), line.split('|')[1].split(), [str()] * 7
    decode.sort(key=cmp_to_key(lambda digit1, digit2: len(digit1) - len(digit2)))
    display[0] = (decode[1] - decode[0]).pop()
    display[4] = (decode[9] - (decode[6].intersection(decode[7].intersection(decode[8]))) - decode[2]).pop()
    display[6] = (decode[9] - set(display[0]) - set(display[4]) - decode[2]).pop()
    display[3] = (decode[3].intersection(decode[4]).intersection(decode[5]) - set(display[0]) - set(display[6])).pop()
    display[1] = (decode[9] - decode[1] - set(display[3]) - set(display[4]) - set(display[6])).pop()
    display[5] = (decode[6].intersection(decode[7].intersection(decode[8])) - set(display[0]) - set(display[1]) - set(display[6])).pop()
    display[2] = (decode[0] - set(display[5])).pop()
    reverse = {display[i]: i for i in range(7)}
    cur = ''
    for digit in digits:
        if len(digit) == 2:
            cur += '1'
        elif len(digit) == 3:
            cur += '7'
        elif len(digit) == 4:
            cur += '4'
        elif len(digit) == 7:
            cur += '8'
        else:
            temp = []
            for char in digit:
                temp.append(reverse[char])
            temp.sort()
            if temp == [0, 1, 2, 4, 5, 6]:
                cur += '0'
            elif temp == [0, 2, 3, 4, 6]:
                cur += '2'
            elif temp == [0, 2, 3, 5, 6]:
                cur += '3'
            elif temp == [0, 1, 3, 5, 6]:
                cur += '5'
            elif temp == [0, 1, 3, 4, 5, 6]:
                cur += '6'
            else:
                cur += '9'
    ans += int(cur)
print(ans)
