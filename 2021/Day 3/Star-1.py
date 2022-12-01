input = open('input', 'r')
nums = input.read().split()
gamma = epsilon = ''
for i in range(len(nums[0])):
    ones = 0
    for num in nums:
        ones += num[i] == '1'
    if ones > len(nums) - ones:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
print(int(gamma, 2) * int(epsilon, 2))
