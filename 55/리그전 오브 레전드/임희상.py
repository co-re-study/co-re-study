N, Q = map(int, input().split())

teams = [0] + list(map(int, input().split()))

prefix_sum = [0]
current = 0
for i in range(N):
    current += teams[i+1]
    prefix_sum.append(current)

dp = [0]
for i in range(1, N+1):
    dp.append(dp[-1] + prefix_sum[i-1]*teams[i])

answer = []
for i in range(Q):
    l, r = map(int, input().split())
    answer.append(str(dp[r] - dp[l-1] - prefix_sum[l-1] * (prefix_sum[r]-prefix_sum[l-1])))

print('\n'.join(answer))