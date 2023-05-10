'''
1자리 있을때 앉는 방법 : 1
2자리 있을때 앉는 방법 : 12 21
3자리 있을때 앉는 방법 : 123 132 213
4자리 있을때 앉는 방법 : 1234 1243 1324 2134 2143
5자리 있을때 앉는 방법 : 12345 12354 12435 13245 13254 21345 21354 21435
피보나치 수열
'''
# 방법 1 : 피보나치 수열 규칙 찾아서 dict 형태로 만들기 (52ms)
def fib(i):
    if not A.get(i):
        if i % 2 == 1:
            A[i] = (fib((i+1)//2)**2+fib(((i+1)//2)-1)**2)
        else:
            A[i] = fib(i+1)-fib(i-1)
    return A[i]

A = {0: 0, 1: 1, 2: 1} # A[n+1] : n자리 있을때 앉는 방법
N = int(input())
M = int(input())
ans = 1
temp = 0
for _ in range(M):
    num = int(input())
    ans *= fib(num-temp)
    temp = num
ans *= fib(N+1-temp)
print(ans)


# 방법 2: 피보나치 dp로 만들기 (40ms)
N = int(input())
dp = [0]*(N+1)
dp[0] = 1
dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-1]+dp[i-2]
M = int(input())
ans = 1
temp = 0
for _ in range(M):
    num = int(input())
    ans *= dp[num-temp-1]
    temp = num
ans *= dp[N-temp]
print(ans)
