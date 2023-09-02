def solution(temperature, t1, t2, a, b, onboard):
    init = max(temperature-t1, t2-temperature)
    dp = [[100000] * (init+2) for _ in range(len(onboard))]
    dp[0][init] = 0
    
    for i in range(1, len(onboard)):
        for j in range(init+1):
            if onboard[i] and j > t2 - t1:
                print(i, j)
                continue
            
            min_cost = dp[i-1][j-1]
            if j:
                min_cost = min(min_cost, dp[i-1][j+1]+a)
            if j == init:
                min_cost = min(min_cost, dp[i-1][j])
            if j <= t2 - t1:
                min_cost = min(min_cost, dp[i-1][j]+b)
            
            dp[i][j] = min_cost
            
    return min(dp[len(onboard)-1])