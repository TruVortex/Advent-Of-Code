arr1, arr2 = [], []
for line in open('input', 'r'):
    left, right = line.split()
    arr1.append(int(left))
    arr2.append(int(right))
total = 0
for num in arr1:
    total += num * arr2.count(num)
print(total)
