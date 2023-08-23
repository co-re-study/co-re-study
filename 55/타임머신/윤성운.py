# 벨만포드

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edge_list = []
for _ in range(M):
    start, end, time = map(int, input().split())
    edge_list.append((start, end, time))

INF = float("inf")
distance = [INF] * (N + 1)
distance[1] = 0

for i in range(N):
    for j in range(M):
        start, end, time = edge_list[j]
        if distance[start] != INF and distance[start] + time < distance[end]:
            distance[end] = distance[start] + time
            if i == N - 1:
                print(-1)
                exit(0)

for i in range(2, N + 1):
    print(distance[i]) if distance[i] != INF else print(-1)

#######################################################################

# SPFA
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, time = map(int, input().split())
    adj_list[start].append((end, time))

INF = float("inf")
queue = deque([1])
cnt_list = [0] * (N + 1)
on_queue = [0] * (N + 1)
distance = [INF] * (N + 1)
distance[1] = 0

while queue:
    current = queue.popleft()
    on_queue[current] = 0
    for dest in adj_list[current]:
        if distance[current] + dest[1] < distance[dest[0]]:
            distance[dest[0]] = distance[current] + dest[1]
            if not on_queue[dest[0]]:
                queue.append(dest[0])
                on_queue[dest[0]] = 1
                cnt_list[dest[0]] += 1
                if cnt_list[dest[0]] == N:
                    print(-1)
                    exit(0)

for i in range(2, N + 1):
    print(distance[i]) if distance[i] != INF else print(-1)
