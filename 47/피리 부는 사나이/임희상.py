N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input()))

direction = {
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1)
}
visited = [[0]*M for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue

        r, c = i, j
        local_visited = set()
        while not visited[r][c]:
            visited[r][c] = 1
            local_visited.add((r, c))
            r += direction[board[r][c]][0]
            c += direction[board[r][c]][1]
        if (r, c) in local_visited:
            answer += 1

print(answer)
