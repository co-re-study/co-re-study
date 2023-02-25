# 동전0
import sys
N, K = map(int, sys.stdin.readline().split())
moneyList = []
for _ in range(N):
    moneyList.append(int(sys.stdin.readline()))
targetIndex = N - 1

answer = 0
while 0 < K:
    money = moneyList[targetIndex]
    if K // money:
        answer += K // money
        K -= money * (K // money)
    targetIndex -= 1
print(answer)