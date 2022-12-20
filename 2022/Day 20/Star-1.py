class Node:

    def __init__(self, val):
        self.val = val
        self.left = self.right = None


vals = list(map(int, open('input', 'r').read().split()))
mod = len(vals)
ans, zero, nums = 0, Node, [Node(vals[i]) for i in range(mod)]
for i in range(mod):
    nums[i].left = nums[(i - 1) % mod]
    nums[i].right = nums[(i + 1) % mod]
mod -= 1
for node in nums:
    if node.val == 0:
        zero = node
        continue
    if node.val % mod == 0:
        continue
    node.left.right = node.right
    node.right.left = node.left
    temp = node
    if node.val > 0:
        for i in range(node.val % mod):
            temp = temp.right
        node.right = temp.right
        node.left = temp
        temp.right.left = node
        temp.right = node
    else:
        for i in range(-node.val % mod):
            temp = temp.left
        node.left = temp.left
        node.right = temp
        temp.left.right = node
        temp.left = node
for i in range(3):
    for j in range(1000):
        zero = zero.right
    ans += zero.val
print(ans)
