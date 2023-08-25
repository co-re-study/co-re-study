N = int(input())

dp = [[[0] * 1024 for _ in range(10)] for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i][1<<i] = 1

for i in range(2, N+1):
    for j in range(10):
        for k in range(1024):
            if j > 0:
                temp = k|(1<<(j-1))
                dp[i][j-1][temp] += dp[i-1][j][k]
                dp[i][j-1][temp] %= 1000000000
            if j < 9:
                temp = k|(1<<(j+1))
                dp[i][j+1][temp] += dp[i-1][j][k]
                dp[i][j+1][temp] %= 1000000000

answer = 0
for i in range(10):
    answer += dp[N][i][-1] 
    answer %= 1000000000

print(answer)