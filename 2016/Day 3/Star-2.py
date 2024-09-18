ans = 0
side1, side2, side3 = [], [], []
for line in open('input', 'r'):
    lengths = list(map(int, line.split()))
    side1.append(lengths[0])
    side2.append(lengths[1])
    side3.append(lengths[2])
for i in range(0, len(side1), 3):
    a, b, c = sorted(side1[i:i+3])
    ans += (a + b > c)
    a, b, c = sorted(side2[i:i+3])
    ans += (a + b > c)
    a, b, c = sorted(side3[i:i+3])
    ans += (a + b > c)
print(ans)
