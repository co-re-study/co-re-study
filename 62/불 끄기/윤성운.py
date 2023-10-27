import sys
from copy import deepcopy
input = sys.stdin.readline

# 나와 주변 전구 바꾸기
def convert(r, c):
    global cnt

    arr[r][c] = "O" if arr[r][c] == "#" else "#"
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 10 and 0 <= nc < 10:
            arr[nr][nc] = "O" if arr[nr][nc] == "#" else "#"
    cnt += 1


n = 10
org_arr = [list(input().strip()) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

answer = 101
# 첫줄은 모든 경우의수 확인
for i in range(1 << n):
    arr = deepcopy(org_arr)
    cnt = 0

    # 현재 경우에 해당하는 전구 스위치 누르기
    for j in range(n):
        if i & (1 << j):
            convert(0, j)

    # 두번째줄부터 윗 줄이 켜져 있으면 스위치 누르기
    for r in range(1, n):
        for c in range(n):
            if arr[r - 1][c] == "O":
                convert(r, c)

    # 맨 마지막 줄에 켜져 있는 전구 없는지 확인
    for c in range(n):
        if arr[n - 1][c] == "O":
            break
    else:
        answer = min(answer, cnt)

if answer == 101:
    print(-1)
else:
    print(answer)
    