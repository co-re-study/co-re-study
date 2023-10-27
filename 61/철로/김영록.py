from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N = int(input())
routes = []
for _ in range(N):
    h, o = map(int, input().split())
    routes.append((min(h, o), max(h, o)))
routes.sort(key=lambda x: (x[1], x[0]))
d = int(input())
ans = 0
queue = []
for route in routes:
    if route[1]-route[0] > d:
        continue
    while queue and queue[0][0]+d < route[1]:
        heappop(queue)
    heappush(queue, route)
    ans = max(ans, len(queue))
print(ans)
