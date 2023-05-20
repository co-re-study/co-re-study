import sys
input = sys.stdin.readline


# 폭탄 시간 줄이기
def reduce_bomb_time():
    for r in range(R):
        for c in range(C):
            if arr[r][c] in {".", 0}:
                continue
            arr[r][c] -= 1


# 폭탄 폭발
def explosion():
    memo = set()
    for r in range(R):
        for c in range(C):
            if not arr[r][c]:
                arr[r][c] = "."
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < R and 0 <= nc < C:
                        memo.add((nr, nc))
    for position in memo:
        arr[position[0]][position[1]] = "."


# 폭탄 설치
def plant_bomb():
    for r in range(R):
        for c in range(C):
            if arr[r][c] ==".":
                arr[r][c] = 3


R, C, N = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
for r in range(R):
    for c in range(C):
        if arr[r][c] == "O":
            arr[r][c] = 3 # 폭탄 시간은 3초

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for time in range(1, N + 1):
    reduce_bomb_time()
    explosion()
    if not time % 2:
        plant_bomb()

answer = [[0] * C for _ in range(R)]
for r in range(R):
    for c in range(C):
        if arr[r][c] == ".":
            answer[r][c] = "."
        else:
            answer[r][c] = "O"

for r in range(R):
    print("".join(answer[r]))