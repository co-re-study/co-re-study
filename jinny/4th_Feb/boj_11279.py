# 최대힙
import heapq
n = int(input())
q = []
for i in range(n):
    x = int(input())
    if x:
        heapq.heappush(q, -x)
    else:
        if q:
            print(heapq.heappop(q) * -1)
        else:
            print(0)