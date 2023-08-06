from collections import deque

INF = 10**9
N, M = map(int, input().split())
Hx, Hy = map(lambda x: int(x) - 1, input().split())
Ex, Ey = map(lambda x: int(x) - 1, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
times = [[[INF, INF] for m in range(M)] for n in range(N)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
q = deque([(Hx, Hy, 1)])
time = 0
times[Hx][Hy] = [0, 0]
visited = set()

while q:
    for _ in range(len(q)):
        x, y, wand = q.popleft()
        times[x][y][wand] = time
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if not maze[nx][ny] and time < times[nx][ny][wand] and (nx, ny, wand) not in visited:
                    q.append((nx, ny, wand))
                    visited.add((nx, ny, wand))
                elif maze[nx][ny] and wand and time < times[nx][ny][0] and (nx, ny, 0) not in visited:
                    q.append((nx, ny, 0))
                    visited.add((nx, ny, 0))
    time += 1

ans = min(times[Ex][Ey])
if ans == INF:
    print(-1)
else:
    print(ans)