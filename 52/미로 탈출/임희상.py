from collections import deque
N, M = map(int, input().split())
start = list(map(lambda x: int(x)-1, input().split()))
end = list(map(lambda x: int(x)-1, input().split()))

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

queue = deque([[start[0], start[1], 0, False]])

visited = {}
answer = 0
while queue:
    r, c, dist, used = queue.popleft()
    if (r, c) in visited.keys():
        if (r, c) in visited.keys():
            if visited[(r, c)] and not used:
                pass
            else:
                continue
            
    if [r, c] == end:
        answer = dist
        break

    visited[(r, c)] = used
    
    for nr, nc in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
        if 0 <= nr < N and 0 <= nc < M:
            if not board[nr][nc]:
                queue.append([nr, nc, dist+1, used])
            else:
                if not used:
                    queue.append([nr, nc, dist+1, True])

if not answer:
    answer = -1

print(answer)