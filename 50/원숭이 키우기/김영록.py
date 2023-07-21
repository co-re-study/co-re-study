# 삽질 코드
# import sys
# N = int(input())
# characters = [0]+list(map(int, input().split()))
# powers = [0]+list(map(int, input().split()))
# days = int(input())
# dp = [[[0 for _ in range(sum(characters)+1)] for _ in range(N+1)] for _ in range(days+1)]

# ans = sum([characters[i]*powers[i] for i in range(1, N+1)])
# for i in range(days+1):
#     for j in range(N, -1, -1):
#         for k in range(i+1):
#             if j == N:
#                 dp[i][j][k] = 0
#                 continue
#             for l in range(min(i, characters[j] + k) + 1):
#                 dp[i][j][k] = max(
#                     dp[i][j][k], dp[i-l][j+1][characters[j] + l] + (powers[j+1] - powers[j])*l)
# print(ans + dp[days][0][0])

import sys
input = sys.stdin.readline
N = int(input())
characters = list(map(int, input().split()))
powers = list(map(int, input().split()))
days = int(input())
dp = [[[-1 for _ in range(days+1)] for _ in range(N)] for _ in range(days+1)]
ans = sum([characters[i]*powers[i] for i in range(N)])
def solution(x, y, z):
    if y == N - 1:
        return 0
    if dp[x][y][z] != -1:
        return dp[x][y][z]

    dp[x][y][z] = 0
    for i in range(z + characters[y] + 1):
        if x < i:
            break
        dp[x][y][z] = max(dp[x][y][z], solution(
            x - i, y + 1, i) + (powers[y + 1] - powers[y]) * i)
    return dp[x][y][z]

print(ans + solution(days, 0, 0))

import sys
input = sys.stdin.readline
N = int(input())
characters = list(map(int, input().split()))
powers = list(map(int, input().split()))
days = int(input())
dp = [[[-1 for _ in range(days+1)] for _ in range(N)] for _ in range(days+1)]
ans = sum([characters[i]*powers[i] for i in range(N)])
stack = [(days, 0, 0)]
while stack:
    x, y, z = stack[-1]
    if dp[x][y][z] != -1:
        stack.pop()
        continue
    if y == N - 1:
        dp[x][y][z] = 0
        stack.pop()
        continue
    flag = False
    for i in range(z + characters[y] + 1):
        if x < i:
            break
        if dp[x - i][y + 1][i] == -1:
            stack.append((x - i, y + 1, i))
            flag = True
    if flag:
        continue
    dp[x][y][z] = 0
    for i in range(z + characters[y] + 1):
        if x < i:
            break
        dp[x][y][z] = max(dp[x][y][z], dp[x - i][y + 1]
                          [i] + (powers[y + 1] - powers[y]) * i)
    stack.pop()
print(ans + dp[days][0][0])
