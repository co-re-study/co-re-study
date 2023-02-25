# 피보나치
# def fibo(n):
#     if not n:
#         answer[0] += 1
#         return 0
#     elif n == 1:
#         answer[1] += 1
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
#
#
# for tc in range(int(input())):
#     answer = [0, 0]
#     fibo(int(input()))
#     print(*answer)

dp = [(1, 0), (0, 1), (1, 1), (1, 2), (2, 3)]
for i in range(5,  41):
    dp.append((dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]))
for tc in range(int(input())):
    print(*dp[int(input())])