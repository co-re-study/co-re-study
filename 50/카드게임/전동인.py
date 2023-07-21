n = int(input())
l = list(map(int, input().split()))
r = list(map(int, input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if l[i] > r[j]:
            # 카드를 오른쪽만 버릴 경우,
            dp[i][j] = dp[i][j+1] + r[j]
        else:
            # 카드를 왼쪽만 버릴 경우, dp[i+1][j]
            # 카드를 둘다 버릴 경우, dp[i+1][j+1]
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])

print(dp[0][0])
