import sys
input = sys.stdin.readline

N = int(input())
memo = [[[0] * 1024 for _ in range(10)] for _ in range(N + 1)]

# 0빼고 나머지 1로 채우고 시작
for i in range(1, 10):
    memo[1][i][1 << i] = 1

# i: 숫자 길이, j: 마지막 숫자, k: 지나온 숫자들
for i in range(2, N + 1):
    for j in range(10):
        if j - 1 >= 0:
            for k in range(1024):
                memo[i][j][k | (1 << j)] = (memo[i][j][k | (1 << j)] + memo[i - 1][j - 1][k]) % 1000000000
        if j + 1 < 10:
            for k in range(1024):
                memo[i][j][k | (1 << j)] = (memo[i][j][k | (1 << j)] + memo[i - 1][j + 1][k]) % 1000000000

answer = 0
for i in range(10):
    answer = (answer + memo[N][i][1023]) % 1000000000
print(answer)
