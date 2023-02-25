import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(n):
    dp[i + 1] = dp[i] + numbers[i]

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[e] - dp[s - 1])