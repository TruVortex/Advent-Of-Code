parsed_input, total = [line.split() for line in open('input', 'r')], 0
for line in parsed_input:
    final, buttons, cnt = [char == '#' for char in line[0][1:-1]], [tuple(map(int, wiring[1:-1].split(','))) for wiring in line[1:-1]], float('inf')
    for mask in range(1 << len(buttons)):
        state = [False] * len(final)
        for i, button in enumerate(buttons):
            if mask & (1 << i):
                for change in button:
                    state[change] ^= True
        if state == final:
            cnt = min(cnt, mask.bit_count())
    total += cnt
print(total)
