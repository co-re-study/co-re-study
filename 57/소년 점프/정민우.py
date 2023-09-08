# 각 악당별로 bfs돌아서 미로 지점별 걸리는 시간 구하기
# 각 지점에 악당이 오는데 걸리는 최대값의 최소값이 정답

from collections import deque

INF = 999999999
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(n, start):
    queue = deque([start])
    t = 0
    visited[start[0]][start[1]][n] = t
    while queue:
        t += 1
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < R and 0 <= nj < C and not maze[ni][nj] and visited[ni][nj][n] == INF:
                    visited[ni][nj][n] = t
                    queue.append((ni, nj))

R, C = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(R)]
villains = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(3)]
visited = [[[999999999] * 3 for c in range(C)] for r in range(R)]

for idx, v in enumerate(villains):
    bfs(idx, v)

ans, count = INF, 1
for r in range(R):
    for c in range(C):
        if max(visited[r][c]) < ans:
            ans = max(visited[r][c])
            count = 1
        elif max(visited[r][c]) == ans:
            count += 1
if ans < INF:
    print(ans)
    print(count)
else:
    print(-1)