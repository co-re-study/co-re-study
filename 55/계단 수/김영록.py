mod = 1000000000
N = int(input())
dp = [[[0]*1024 for _ in range(10)] for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i][1 << i] = 1
for k in range(2, N+1):
    for i in range(10):
        for j in range(1024):
            if i > 0:
                dp[k][i][j | (1 << i)] += dp[k-1][i-1][j] % mod
            if i < 9:
                dp[k][i][j | (1 << i)] += dp[k-1][i+1][j] % mod
print(sum(dp[N][i][1023] for i in range(10)) % mod)
