def count(new_springs, new_records):
    global memoize
    if len(new_springs) == 0:
        return len(new_records) == 0
    if len(new_records) == 0:
        return '#' not in new_springs
    key = (new_springs, new_records)
    if key in memoize:
        return memoize[key]
    total = 0
    if new_springs[0] in '.?':
        total += count(new_springs[1:], new_records)
    if new_springs[0] in '?#' and len(new_springs) >= new_records[0] and '.' not in new_springs[:new_records[0]] and (len(new_springs) == new_records[0] or new_springs[new_records[0]] != '#'):
        total += count(new_springs[new_records[0] + 1:], new_records[1:])
    memoize[key] = total
    return total


cnt, memoize = 0, {}
for line in open('input', 'r'):
    springs, records = line.split()
    cnt += count('?'.join([springs] * 5), tuple(map(int, records.split(','))) * 5)
print(cnt)
