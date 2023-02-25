# 123더하기
for tc in range(int(input())):
    dp = [0, 1, 2, 4, 7, 13, 24]
    for i in range(7, 11):
        dp.append(sum(dp[i-3:i]))
    print(dp[int(input())])