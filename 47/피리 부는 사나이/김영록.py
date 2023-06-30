dic = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
N, M = map(int, input().split())
maps = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        x, y = i, j
        temp = set()
        while not visited[x][y]:
            visited[x][y] = 1
            temp.add((x, y))
            x += dic[maps[x][y]][0]
            y += dic[maps[x][y]][1]
        if (x, y) in temp:
            ans += 1
print(ans)
