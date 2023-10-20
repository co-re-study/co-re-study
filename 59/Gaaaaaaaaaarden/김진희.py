from collections import deque
import sys

input = sys.stdin.readline


def cur(depth, r, b, red, blue, start):
    if depth == G + R:
        solve(red, blue)
        return

    for i in range(start, len(possible)):
        if r:
            cur(depth + 1, r - 1, b, red + [possible[i]], blue, i + 1)
        if b:
            cur(depth + 1, r, b - 1, red, blue + [possible[i]], i + 1)


def solve(red, blue):
    global answer
    table = [[0] * M for _ in range(N)]
    for r, c in red:
        table[r][c] = 1
    for r, c in blue:
        table[r][c] = 2

    cnt = 0
    red = deque(red)
    blue = deque(blue)
    while red and blue:
        for day in range(len(red)):
            cr, cc = red.popleft()
            if table[cr][cc] != 99999:
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 0 and table[nr][nc] == 0:
                        red.append((nr, nc))
                        table[nr][nc] = table[cr][cc] + 2

        for day in range(len(blue)):
            cr, cc = blue.popleft()
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 0:
                    if table[nr][nc] == 0:
                        blue.append((nr, nc))
                        table[nr][nc] = table[cr][cc] + 2
                    elif table[nr][nc] == table[cr][cc] + 1:
                        table[nr][nc] = 99999
                        cnt += 1
    answer = max(answer, cnt)


N, M, G, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # 0호수 1배양액x 2배양액가능

# 배양액을 뿌릴 수 있는 땅을 찾고
possible = []
room = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            possible.append((i, j))
        if arr[i][j] != 0:
            room += 1

answer = 0
cur(0, R, G, [], [], 0)
print(answer)
