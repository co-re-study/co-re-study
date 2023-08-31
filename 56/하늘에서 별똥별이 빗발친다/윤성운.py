import sys
input = sys.stdin.readline

# lower bound 이분 탐색
def min_binary_search(array, idx, target):
    left = 0
    right = K
    while left < right:
        middle = (left + right) // 2
        if array[middle][idx] >= target:
            right = middle
        else:
            left = middle + 1
    return left


# upper bound 이분 탐색
def max_binary_search(array, idx, target):
    left = 0
    right = K
    while left < right:
        middle = (left + right) // 2
        if array[middle][idx] > target:
            right = middle
        else:
            left = middle + 1
    return left
        

N, M, L, K = map(int, input().split())
positions = [tuple(map(int, input().split())) for _ in range(K)]

sorted_by_rows = sorted(positions, key=lambda x: x[0])
sorted_by_cols = sorted(positions, key=lambda x: x[1])

# 가능한 모든 row와 col 조합 만들기
trampoline_positions = set()
for i in range(K):
    for j in range(K):
        if positions[i][0] <= positions[j][0] and positions[j][1] <= positions[i][1]:
            if positions[j][0] - positions[i][0] <= L and positions[i][1] - positions[j][1] <= L:
                trampoline_positions.add((positions[i][0], positions[j][1]))

# 주어진 범위 내 떨어지는 별의 개수 구하기
max_cnt = 1
for position in trampoline_positions:
    min_r_idx = min_binary_search(sorted_by_rows, 0, position[0])
    max_r_idx = max_binary_search(sorted_by_rows, 0, position[0] + L)
    min_c_idx = min_binary_search(sorted_by_cols, 1, position[1])
    max_c_idx = max_binary_search(sorted_by_cols, 1, position[1] + L)

    max_cnt = max(max_cnt, len(set(sorted_by_rows[min_r_idx: max_r_idx]) & set(sorted_by_cols[min_c_idx: max_c_idx])))

print(K - max_cnt)