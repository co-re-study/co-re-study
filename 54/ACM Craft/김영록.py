import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time = [0]+list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    indegree = [0]*(N+1)
    dp = [0]*(N+1)
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1
    W = int(input())
    queue = deque()
    for i in range(1, N+1):
        if not indegree[i]:
            queue.append(i)
            dp[i] = time[i]
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now]+time[i])
            if not indegree[i]:
                queue.append(i)
    print(dp[W])
