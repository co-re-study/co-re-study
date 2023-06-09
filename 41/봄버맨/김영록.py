from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()
        arr[x][y] = '.'
        for i in range(4):
            x1 = x+dx[i]
            y1 = y+dy[i]
            if 0 <= x1 < R and 0 <= y1 < C and arr[x1][y1] == 'O':
                arr[x1][y1] = '.'


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
R, C, N = map(int, input().split())
arr = [list(input()) for _ in range(R)]
queue = deque()
for i in range(1, N+1):
    if i == 1:
        for i in range(R):
            for j in range(C):
                if arr[i][j] == 'O':
                    queue.append([i, j])
    elif i % 2:
        bfs()
        for i in range(R):
            for j in range(C):
                if arr[i][j] == 'O':
                    queue.append([i, j])
    else:
        arr = [['O']*C for _ in range(R)]
for a in arr:
    print(''.join(a))