def make_tree(tree, node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]

    middle = (start + end) // 2
    left = make_tree(tree, node * 2, start, middle)
    right = make_tree(tree, node * 2 + 1, middle + 1, end)
    tree[node] = left * right % 1000000007
    return tree[node]


def update_tree(idx, value, node, start, end):
    if idx < start or end < idx:
        return stree[node]

    if start == end:
        stree[node] = value
        return stree[node]

    middle = (start + end) // 2
    left = update_tree(idx, value, node * 2, start, middle)
    right = update_tree(idx, value, node * 2 + 1, middle + 1, end)
    stree[node] = left * right % 1000000007
    return stree[node]


def find_node(start, end, node, left, right):
    if end < left or right < start:
        return 1
    if start <= left and right <= end:
        return stree[node]
    middle = (start + end) // 2
    left_value = find_node(start, end, node * 2, left, middle)
    right_value = find_node(start, end, node * 2 + 1, middle + 1, right)
    return left_value * right_value % 1000000007


N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

# [1] 세그먼트 트리 만들기
stree = [0 for _ in range(N * 4)]
make_tree(stree, 1, 0, N - 1)

for tc in range(M + K):
    command, b, c = map(int, input().split())
    # [2] 세그먼트 트리 수정
    if command == 1:
        update_tree(b - 1, c, 1, 0, N - 1)
    # [3] 구간 곱 출력
    else:
        print(find_node(b - 1, c - 1, 1, 0, N - 1) % 1000000007)
