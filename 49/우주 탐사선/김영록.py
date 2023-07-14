def backtracking(current, depth, time):
    global ans
    if depth == N:
        ans = min(ans, time)
        return
    for target in range(N):
        if not visited[target]:
            visited[target] = 1
            backtracking(target, depth+1, time+arr[current][target])
            visited[target] = 0


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])
visited = [0]*N
visited[K] = 1
ans = 100000
backtracking(K, 1, 0)
print(ans)
