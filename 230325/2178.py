from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

q = deque()
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
visited = set()
finish = (N - 1, M - 1)
result = 9999
cnt = 1
flag = True
q.append((0, 0))
visited.add((0, 0))

while q and flag:
    cnt += 1
    for _ in range(len(q)):
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if maze[nr][nc] == 0 or (nr, nc) in visited:
                continue
            visited.add((nr, nc))
            q.append((nr, nc))
            if (nr, nc) == finish:
                flag = False
                break

print(cnt)