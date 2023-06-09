T, W = map(int, input().split(" "))

plum = [0] + [int(input()) for _ in range(T)]

dp = [[0] * (W + 1) for _ in range(T + 1)]

# 한번도 안움직이는 경우
for i in range(T + 1):
    # 1번 나무에서 떨어진 경우
    if plum[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    # 2번 나무에서 떨어진 경우
    else:
        dp[i][0] = dp[i-1][0]

    # 움직이는 경우
    for j in range(1, W + 1):
        # 홀수번일 때
        if plum[i] == 2 and (j % 2):
            # 움직일건지 말건지를 비교, 이전에 그대로 있던것과 움직였던 것 중에 큰 값에 더해줌
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
        # 0 또는 짝수번일 때
        elif plum[i] == 1 and (not j % 2):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
        # 못 움직이거나 안 움직였을 때
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[T]))