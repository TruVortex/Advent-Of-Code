input = open('input', 'r')
oxygen = input.read().split()
co2 = oxygen.copy()
check: str
for i in range(len(oxygen[0])):
    ones = zeros = 0
    if len(oxygen) != 1:
        for num in oxygen:
            ones += num[i] == '1'
        if ones >= len(oxygen) - ones:
            check = '0'
        else:
            check = '1'
        for j in range(len(oxygen) - 1, -1, -1):
            if oxygen[j][i] == check:
                oxygen.pop(j)
    if len(co2) != 1:
        for num in co2:
            zeros += num[i] == '0'
        if zeros <= len(co2) - zeros:
            check = '1'
        else:
            check = '0'
        for j in range(len(co2) - 1, -1, -1):
            if co2[j][i] == check:
                co2.pop(j)
print(int(oxygen[0], 2) * int(co2[0], 2))
