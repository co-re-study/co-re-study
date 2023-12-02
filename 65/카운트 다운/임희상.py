def solution(target):
    answer = []
    
    scores = list(range(1, 21))
    dp = [[float('INF'), 0] for _ in range(target + 1)]
    dp[0] = [0, 0]
    
    for k in [2, 3]:
        for i in scores:
            i *= k
            for j in range(i, target + 1):
                if dp[j - i][0] + 1 < dp[j][0]:
                    dp[j] = [dp[j - i][0] + 1, dp[j - i][1]]
    
    for i in scores + [50]:
        for j in range(i, target + 1):
            if dp[j - i][0] + 1 < dp[j][0]:
                dp[j] = [dp[j - i][0] + 1, dp[j - i][1] + 1]
            elif dp[j - i][0] + 1 == dp[j][0] and dp[j - i][1] + 1 > dp[j][1]:
                dp[j][1] = dp[j - i][1] + 1
    
    return dp[-1]