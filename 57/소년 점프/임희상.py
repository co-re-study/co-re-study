from collections import deque

R, C = map(int, input().split())

board = []

for _ in range(R):
    board.append(list(map(int, list(input()))))

result = [[[-1, -1, -1] for _ in range(C)] for _ in range(R)]

def bfs(start, idx):

    queue = deque([[start[0]-1, start[1]-1, 0]])
    visited = set()

    while queue:
        r, c, dist = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        result[r][c][idx] = dist
        for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and not board[nr][nc] and (nr, nc) not in visited:
                queue.append([nr, nc, dist+1])

for idx in [0, 1, 2]:
    bfs(list(map(int, input().split())), idx)

answer = -1
counts = 0
for r in range(R):
    for c in range(C):
        if -1 not in result[r][c]:
            # 조건
            if max(result[r][c]) < answer:
                answer = max(result[r][c])
                counts = 1
            elif max(result[r][c]) == answer:
                counts += 1
            if answer == -1:
                answer = max(result[r][c])
                counts = 1

print(answer)
if answer != -1:
    print(counts)
