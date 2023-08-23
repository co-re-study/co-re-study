import sys
input = sys.stdin.readline

# 네 좌표 찍기
def acc(r_start, c_start, r_end, c_end, degree):
    acc_arr[r_start][c_start] += degree
    acc_arr[r_end][c_start] -= degree
    acc_arr[r_start][c_end] -= degree
    acc_arr[r_end][c_end] += degree


M, N = map(int, input().split())
acc_arr = [[0] * (M + 1) for _ in range(M + 1)]
grow_dict = dict()

for _ in range(N):
    grow_info = list(map(int, input().split()))

    # 모든 조건에 따라 누적합 배열에 직접 네 좌표 표시
    if grow_info[2] >= M:
        acc(0, 0, M, M, 2)
        if grow_info[1]:
            acc(M - (grow_info[0] + grow_info[1]), 0, M, 1, -1)
            if grow_info[0]:
                acc(M - grow_info[0], 0, M, 1, -1)
        elif grow_info[0]:
            acc(M - grow_info[0], 0, M, 1, -2)
    else:
        if grow_info[1] + grow_info[2] >= M:
            acc(0, 0, M, M - grow_info[2], 1)
            if grow_info[0]:
                acc(M - grow_info[0], 0, M, 1, -1)
        elif grow_info[1]:
            acc(0, M - (grow_info[1] + grow_info[2]), M, M - grow_info[2], 1)
        if grow_info[2]:
            acc(0, M - grow_info[2], M, M, 2)

# 누적합
for r in range(M + 1):
    for c in range(1, M + 1):
        acc_arr[r][c] += acc_arr[r][c - 1]
for c in range(M + 1):
    for r in range(1, M + 1):
        acc_arr[r][c] += acc_arr[r - 1][c]

for r in range(M):
    for c in range(M):
        acc_arr[r][c] += 1

for r in range(M):
    print(" ".join(map(str, acc_arr[r][:-1])))
