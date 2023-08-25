import sys
input=sys.stdin.readline

M, N = map(int, input().split())
arr = [[1 for _ in range(M)] for _ in range(M)]
growth_list = [0 for _ in range(M*2-1)]
for i in range(N):
    zero_cnt, one_cnt, two_cnt = map(int, input().split())
    for j in range(zero_cnt, zero_cnt+one_cnt):
        growth_list[j] += 1
    for j in range(zero_cnt+one_cnt, M*2-1):
        growth_list[j] += 2

for i in range(M*2-1):
    if i < M:
        arr[(M-1)-i][0] += growth_list[i]
    else:
        arr[0][(i+1)-M] += growth_list[i]

for i in range(1, M):
    for j in range(1, M):
        arr[i][j] = arr[0][j]

for i in range(M):
    print(*arr[i])



