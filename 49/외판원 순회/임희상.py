N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dp = [[0]*(1<<N) for _ in range(N)]

def tsp(current, visited):

    if visited == (1<<N)-1:
        if board[current][0]:
            return board[current][0]
        return float('INF')
    
    if dp[current][visited]:
        return dp[current][visited]
    
    dp[current][visited] = float('INF')

    for i in range(1, N):
        if (visited & (1<<i)) or not board[current][i]:
            continue
        dp[current][visited] = min(dp[current][visited], tsp(i, visited|(1<<i)) + board[current][i])
    return dp[current][visited]

print(tsp(0, 1))