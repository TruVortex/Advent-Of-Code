input = open('input', 'r')
ans = 0
for line in input:
    nums = list(map(int, line.strip().replace(',', '-').split('-')))
    if (nums[0] <= nums[2] <= nums[3] <= nums[1]) or (nums[2] <= nums[0] <= nums[1] <= nums[3]):
        ans += 1
print(ans)
