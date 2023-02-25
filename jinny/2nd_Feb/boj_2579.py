# 계단오르기
n = int(input())  # 계단 수
stair = [0]
for _ in range(n):
    stair.append(int(input()))
dp = [0, stair[1]]
if n > 1:
    dp.append(stair[1] + stair[2])
for i in range(3, n-1):
    dp.append(max(dp[i-3]+stair[i-1]+stair[i], dp[i-2] + stair[i]))

if n == 2:
    print(dp[n])
elif n == 1:
    print(stair[1])
else:
    print(max(dp[n-3]+stair[n-1]+stair[n], dp[n-2] + stair[n]))