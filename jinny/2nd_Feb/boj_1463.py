n = int(input())
answer = 10 ^ 6
#     0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
dp = [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3]
for i in range(11, n + 1):
    if not i % 3 and not i % 2:
        dp.append(min(dp[i - 1] + 1, dp[i//3] + 1, dp[i//2] + 1))
    elif not i % 3:
        dp.append(min(dp[i - 1] + 1, dp[i // 3] + 1))
    elif not i % 2:
        dp.append(min(dp[i - 1] + 1, dp[i // 2] + 1))
    else:
        dp.append(dp[i - 1] + 1)

print(dp[n])