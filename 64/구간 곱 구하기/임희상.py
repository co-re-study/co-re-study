def make_tree(tree, nums, left, right, node):
    if left == right:
        tree[node] = nums[left]
        return tree[node]
    middle = (left + right) // 2
    left_tree = make_tree(tree, nums, left, middle, node * 2)
    right_tree = make_tree(tree, nums, middle + 1, right, node * 2 + 1)
    tree[node] = left_tree * right_tree % 1000000007
    return tree[node]

def update_tree(tree, nums, left, right, idx, node):
    if idx < left or idx > right:
        return tree[node]
    if left == right:
        tree[node] = nums[idx]
        return tree[node]
    middle = (left + right) // 2
    left_tree = update_tree(tree, nums, left, middle, idx, node * 2)
    right_tree = update_tree(tree, nums, middle + 1, right, idx, node * 2 + 1)
    tree[node] = left_tree * right_tree % 1000000007
    return tree[node]

def get_num(tree, left, right, start, end, node):
    if right < start or left > end:
        return 1
    if left >= start and right <= end:
        return tree[node]
    middle = (left + right) // 2
    return (get_num(tree, left, middle, start, end, node * 2) 
            * get_num(tree, middle + 1, right, start, end, node * 2 + 1) 
            % 1000000007)

n, m, k = map(int, input().split())
nums = [0] + [int(input()) for _ in range(n)]
tree = [0] * (n * 4)

make_tree(tree, nums, 1, n, 1)

for _ in range(m + k):
    inputs = list(map(int, input().split()))
    if inputs[0] == 1:
        idx, num = inputs[1], inputs[2]
        nums[idx] = num
        update_tree(tree, nums, 1, n, idx, 1)
    else:
        print(get_num(tree, 1, n, inputs[1], inputs[2], 1))