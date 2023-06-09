T, W = map(int, input().split())
plums = []
for t in range(T):
    plums.append(int(input()))

dp = [[[0, 0] for _ in range(T)] for _ in range(W+1)]
if plums[0] == 1:
    for t in range(T):
        dp[0][t][0] = 1
    for w in range(W+1):
        dp[w][0][0] = 1
else:
    for w in range(1, W+1):
        dp[w][0][1] = 1

for t in range(1, T):
    if plums[t] == 1:
        dp[0][t][0] = dp[0][t-1][0] + 1
    else:
        dp[0][t][0] = dp[0][t-1][0]

for t in range(1, T):
    for w in range(1, W+1):
        if plums[t] == 1:
            dp[w][t][0] = max(dp[w][t-1][0]+1, dp[w-1][t-1][1]+1)
            dp[w][t][1] = max(dp[w][t - 1][1], dp[w-1][t - 1][0])
        else:
            dp[w][t][1] = max(dp[w][t-1][1]+1, dp[w-1][t-1][0]+1)
            dp[w][t][0] = max(dp[w][t - 1][0], dp[w-1][t - 1][1])

# for w in range(W+1):
#     print(dp[w])

print(max(dp[W][T-1]))
