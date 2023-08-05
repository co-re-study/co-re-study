from collections import deque


def m1(x):
    return int(x) - 1


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())
Hx, Hy = map(m1, input().split())
Ex, Ey = map(m1, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[[-1]*2 for _ in range(M)] for _ in range(N)]
visited[Hx][Hy][0] = 0  # x값, y값, 벽뚫 안뚫
queue = deque([[Hx, Hy, 0]])
while queue:
    x, y, destroy = queue.popleft()
    if x == Ex and y == Ey:
        print(visited[x][y][destroy])
        break
    for i in range(4):
        x1 = x+dx[i]
        y1 = y+dy[i]
        if 0 <= x1 < N and 0 <= y1 < M:
            if arr[x1][y1] == 0 and visited[x1][y1][destroy] == -1:
                visited[x1][y1][destroy] = visited[x][y][destroy]+1
                queue.append([x1, y1, destroy])
            elif arr[x1][y1] == 1 and destroy == 0:
                visited[x1][y1][1] = visited[x][y][0]+1
                queue.append([x1, y1, 1])
else:
    print(-1)
