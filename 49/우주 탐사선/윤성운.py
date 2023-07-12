import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

INF = 987654321
# 행: 현재 행성 번호, 열: 방문했던 행성들 비트 마스킹
distance = [[INF] * N for _ in range(1 << N)]
queue = deque([(K, 0, 1 << K)])

# BFS
while queue:
    current, cost, visited = queue.popleft()
    if cost > distance[visited][current]:
        continue

    for destination in range(N):
        if destination == current:
            continue
        if cost + arr[current][destination] < distance[visited | (1 << destination)][destination]:
            distance[visited | (1 << destination)][destination] = cost + arr[current][destination]
            queue.append((destination, cost + arr[current][destination], visited | (1 << destination)))
            
print(min(distance[-1]))

