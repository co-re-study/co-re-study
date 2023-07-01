import sys


def dfs(x, d):
    depth[x] = d
    visited[x] = 1
    for child in routes[x]:
        if visited[child]:
            continue
        parent[child][0] = x
        dfs(child, d+1)


sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N = int(input())
routes = [[] for _ in range(N+1)]
parent = [[0]*17 for _ in range(N+1)]
depth = [0]*(N+1)
visited = [0]*(N+1)
for _ in range(N-1):
    s, e = map(int, input().split())
    routes[s].append(e)
    routes[e].append(s)
dfs(1, 0)
for i in range(1, 17):
    for j in range(1, N+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]
        # 조상 찾아서 올라가는 과정 만들기
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(16, -1, -1):
        if depth[b] - depth[a] >= 2**i:
            b = parent[b][i]
            # depth 같게 만들어주는 과정
    if a == b:
        print(a)
        continue
    for i in range(16, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
            # 조상 찾아서 올라가는 과정
    print(parent[a][0])
