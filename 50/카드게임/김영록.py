import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))  # 왼
B = list(map(int, input().split()))  # 오
dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        if A[i] > B[j]:
            dp[i][j] = max(dp[i+1][j+1], dp[i+1][j], dp[i][j+1]+B[j])
        else:
            dp[i][j] = max(dp[i+1][j+1], dp[i+1][j])
print(dp[0][0])
'''
왼쪽만 버리거나 양쪽 다 버리거나
오른쪽이 더 작으면 오른쪽만 버릴 수 있음. 오른쪽 버리면 오른쪽 점수 얻는다
Top-down 안되서 Bottom-up으로 바꾸니까 됨;
'''
