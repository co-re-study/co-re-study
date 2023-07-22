import sys
sys.setrecursionlimit(1000000)

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[-1]*N for _ in range(N)]

def flip(a, b):

    if a == N or b == N:
        return 0
    
    if dp[a][b] > -1:
        return dp[a][b]
    
    if A[a] <= B[b]:
        dp[a][b] = max(flip(a+1, b), flip(a+1, b+1))
    else:
        dp[a][b] = flip(a, b+1) + B[b]
    
    return dp[a][b]

flip(0, 0)
print(dp[0][0])
