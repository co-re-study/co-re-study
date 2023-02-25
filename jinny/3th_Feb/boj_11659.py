# 구간 합 구하기 4
n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))
dp = [0]
# print(nums)
for _ in range(m):
    i, j = map(int, input().split())
    if len(dp) <= j:
        for z in range(len(dp), j+1):
            dp.append(dp[z-1] + nums[z])
    print(dp[j] - dp[i-1])