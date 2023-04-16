N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 1
right = 2000000000
while left <= right:
    mid = (left + right) // 2
    trees_length = 0
    for tree in trees:
        if tree > mid:
            trees_length += tree - mid

        if trees_length >= M:
            left = mid + 1
            break

    if trees_length < M:
        right = mid - 1

print(left-1)