from collections import deque
import sys
input=sys.stdin.readline

def bfs(current):
    q = deque()
    q.append((current[0], current[1], 0, 0))
    visited = [[[False for _ in range(2)] for _ in range(M)] for _ in range(N)]
    visited[current[0]][current[1]][0] = True
    while q:
        x, y, cnt, used = q.popleft()
        if (x, y) == exit_position:
            return cnt
        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny][used]:
                    continue
                if miro[nx][ny] == 1 and used == 0:
                    visited[nx][ny][1] = True
                    q.append((nx, ny, cnt+1, 1))
                elif miro[nx][ny] == 0:
                    visited[nx][ny][used] = True
                    q.append((nx, ny, cnt+1, used))
    return -1


direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
current = tuple(map(int, input().split()))
exit_position = tuple(map(int, input().split()))
miro = []
for i in range(N):
    miro.append(list(map(int, input().split())))

current = (current[0]-1, current[1]-1)
exit_position = (exit_position[0]-1, exit_position[1]-1)
answer = bfs(current)
print(answer)

