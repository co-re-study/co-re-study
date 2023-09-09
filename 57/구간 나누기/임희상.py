N, M = map(int, input().split())
prefix_sum = [0]
dp = [[0]*(M+1) for _ in range(N+1)]
for j in range(1, M+1):
    dp[0][j] = -float('INF')
for _ in range(N):
    prefix_sum.append(prefix_sum[-1]+int(input()))
    
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j]
        if j == 1:
            dp[i][j] = max(dp[i][j], prefix_sum[i])

        for k in range(2, i+1):
            dp[i][j] = max(dp[i][j], dp[k-2][j-1]+prefix_sum[i]-prefix_sum[k-1])

print(dp[N][M])