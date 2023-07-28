from collections import deque


def check_duplication():
    for i in range(N):
        for j in range(M):
            if not board[i][j] or visited[i][j]:
                continue
            queue = deque([[i, j]])
            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    if x == 0 and d == 1:
                        continue
                    if x == N-1 and d == 0:
                        continue
                    x1 = x+dx[d]
                    y1 = (y+dy[d]) % M
                    if 0 <= x1 < N and board[x][y] == board[x1][y1] and not visited[x1][y1]:
                        visited[x][y] = 1
                        visited[x1][y1] = 1
                        queue.append([x1, y1])


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N, M, T = map(int, input().split())
board = [deque(list(map(int, input().split()))) for _ in range(N)]
rotate_info = [list(map(int, input().split())) for _ in range(T)]
for x, d, k in rotate_info:
    for i in range(N):
        if not (i+1) % x:  # 회전
            if d:
                board[i].rotate(-k)
            else:
                board[i].rotate(k)
    visited = [[0]*M for _ in range(N)]
    check_duplication()
    flag = True
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                board[i][j] = 0
                flag = False
    if flag:
        num = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j]:
                    num += board[i][j]
                    cnt += 1
        if cnt:
            avg = num/cnt
            for i in range(N):
                for j in range(M):
                    if board[i][j] and board[i][j] > avg:
                        board[i][j] -= 1
                    elif board[i][j] and board[i][j] < avg:
                        board[i][j] += 1
ans = 0
for i in board:
    ans += sum(i)
print(ans)
