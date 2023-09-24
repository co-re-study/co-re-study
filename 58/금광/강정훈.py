N = int(input())
parents = [0, 0] + list(map(int, input().split()))
rootCnt = [0 for _ in range(N+1)]
evenCnt = 0
oddCnt = 0
for i in range(1, N+1):
    cnt = 1
    current = parents[i]
    while current != 0:
        if rootCnt[current]:
            cnt += rootCnt[current]
            break
        current = parents[current]
        cnt += 1
    rootCnt[i] = cnt
    if cnt % 2 == 0:
        evenCnt += 1
    else:
        oddCnt += 1
print(min(evenCnt, oddCnt) + abs(evenCnt - oddCnt))