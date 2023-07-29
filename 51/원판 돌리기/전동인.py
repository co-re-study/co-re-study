from collections import deque

n, m, t = map(int, input().split())
circles = [deque(map(int, input().split())) for _ in range(n)]
commands = [list(map(int, input().split())) for _ in range(t)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for x, d, k in commands:
    # 1. 회전
    for i in range(x-1, n, x):
        circles[i].rotate(k if d == 0 else -k)

    # 2. 같은 숫자 제거
    is_removed = False
    check = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if circles[i][j] == 0:
                continue
            for direction in range(4):
                nx, ny = i + dx[direction], (j + dy[direction]) % m
                if nx < 0 or nx >= n:
                    continue
                if circles[nx][ny] == circles[i][j]:
                    check[nx][ny] = check[i][j] = 1
                    is_removed = True
    if is_removed:
        for i in range(n):
            for j in range(m):
                if check[i][j]:
                    circles[i][j] = 0
    else:
        # 3. 같은 수가 없으면 평균보다 큰수 -1, 작은수 +1
        total, count = 0, 0
        for i in range(n):
            for j in range(m):
                if circles[i][j] > 0:
                    total += circles[i][j]
                    count += 1
        average = total / count if total > 0 else 0
        for i in range(n):
            for j in range(m):
                if circles[i][j] > 0:
                    if circles[i][j] > average:
                        circles[i][j] -= 1
                    elif circles[i][j] < average:
                        circles[i][j] += 1

print(sum(map(sum, circles)))
