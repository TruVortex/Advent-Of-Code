arr1, arr2 = [], []
for line in open('input', 'r'):
    left, right = line.split()
    arr1.append(int(left))
    arr2.append(int(right))
arr1.sort()
arr2.sort()
total = 0
for (left, right) in zip(arr1, arr2):
    total += abs(left - right)
print(total)
