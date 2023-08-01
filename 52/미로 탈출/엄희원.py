# 잘 이해가 안됨ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

si, sj = map(int, input().split())

ei, ej = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

ans = -1

visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]
queue = deque()
queue.append([si-1, sj-1, 1, 0])
visited[1][si-1][sj-1] = True


while queue:
    i, j, check, cnt = queue.popleft()
    if i == ei - 1 and j == ej - 1:
        ans = cnt
        break

    for k in range(4):
        r = i + dy[k]
        c = j + dx[k]
        if 0 <= r < N and 0 <= c < M:
            if check:
                if not mat[r][c]:
                     if not visited[1][r][c]:
                        visited[1][r][c] = True
                        queue.append([r, c, check, cnt+1])
                elif mat[r][c]:
                    if not visited[0][r][c]:
                        visited[0][r][c] = True
                        check = 0
                        queue.append([r, c, check, cnt+1])
                        check = 1
            elif not check:
                if not visited[1][r][c] and not visited[0][r][c]:
                    if mat[r][c] == 0:
                        visited[0][r][c] = True
                        queue.append([r, c, check, cnt+1])


print(ans)