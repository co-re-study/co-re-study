import sys
input = sys.stdin.readline

N, K = map(int, input().split())

num = N
memo = set()
answer = 1
while num % K:
    # 현재 숫자에서 K를 나눈 나머지에 원본 숫자를 붙인다.
    num = int(str(num % K) + str(N))
    if num in memo:
        answer = -1
        break
    memo.add(num)
    answer += 1

print(answer)
    