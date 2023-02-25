# 2xn 타일링
# n = int(input())
# dp = [0, 1, 2, 3, 5]
# for i in range(5, n + 1):
#     dp.append(dp[i - 1] + dp[i - 2])
# print(dp[n] % 10007)

# 2×n 타일링 2
n = int(input())
dp = [0, 1, 3, 5, 11]
for i in range(5, n + 1):
    dp.append(dp[i - 1] + dp[i - 2] * 2)
print(dp[n] % 10007)