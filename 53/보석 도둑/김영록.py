from heapq import *
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
heapify(jewels)
bags.sort()
ans = 0
queue = []
for bag in bags:
    while jewels:
        if jewels[0][0] <= bag:
            heappush(queue, -heappop(jewels)[1])
        else:
            break
    if queue:
        ans -= heappop(queue)
print(ans)
