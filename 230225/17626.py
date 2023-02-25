n = int(input())
dp = [0] * (n + 1)
square_nums = [i ** 2 for i in range(1, 224)]

for i in range(1, n + 1):
    if i in square_nums:
        dp[i] = 1
    else:
        dp[i] = min([dp[i - square_nums] for square_nums in square_nums if i - square_nums > 0]) + 1

print(dp[n])


# n = int(input())
# dp = [0] * (n + 1)
# dp[1] = 1
# for i in range(2, n + 1):
#     min_val = float('inf')
#     for j in range(1, int(i ** 0.5) + 1):
#         min_val = min(min_val, dp[i - j ** 2])
#     dp[i] = min_val + 1
#
# print(dp[n])