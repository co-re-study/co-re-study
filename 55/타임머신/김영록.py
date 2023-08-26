import sys


def Bellman_Ford():
    dist[1] = 0
    for i in range(N):
        for j in range(1, N+1):
            for arr, cost in route[j]:
                if dist[j] != INF and dist[arr] > dist[j]+cost:
                    dist[arr] = dist[j]+cost
                    if i == N-1:
                        return True
    return False


input = sys.stdin.readline
INF = 987654321
N, M = map(int, input().split())
route = [[] for _ in range(N+1)]
dist = [INF for _ in range(N+1)]
for j in range(M):
    A, B, C = map(int, input().split())
    route[A].append((B, C))
if Bellman_Ford():
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
