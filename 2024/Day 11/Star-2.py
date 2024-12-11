def process(stone, cycle):
    global memoize
    if cycle == 0:
        return 1
    if (stone, cycle) not in memoize:
        if stone == 0:
            memoize[(stone, cycle)] = process(1, cycle - 1)
        elif len(str(stone)) % 2 == 0:
            memoize[(stone, cycle)] = process(int(str(stone)[:len(str(stone)) // 2]), cycle - 1) + process(int(str(stone)[len(str(stone)) // 2:]), cycle - 1)
        else:
            memoize[(stone, cycle)] = process(stone * 2024, cycle - 1)
    return memoize[(stone, cycle)]



stones, memoize = list(map(int, open('input', 'r').read().split())), {}
print(sum(process(stone, 75) for stone in stones))
