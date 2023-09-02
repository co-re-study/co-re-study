def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    temperature, t1, t2, = temperature + 10, t1 + 10, t2 + 10
    INF = 10**9
    dp = [[INF for _ in range(52)] for _ in range(len(onboard)+1)]
    dp[0][temperature] = 0
    # 가장 상위에 시간초 적용
    # 현재 온도에서 올리거나 유지하거나, 내릴지
    for i in range(1, len(onboard)):
        if onboard[i] == 1:
            start, end = t1, t2
        else:
            start, end = 0, 50

        for j in range(start, end+1):
            if temperature == j:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
            elif temperature > j:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j] + b, dp[i-1][j+1] + a)
            else:
                dp[i][j] = min(dp[i-1][j-1] + a, dp[i-1][j] + b, dp[i-1][j+1])
    answer = min(dp[len(onboard)-1])
    return answer