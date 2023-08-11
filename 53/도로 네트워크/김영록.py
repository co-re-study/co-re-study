import sys
input = sys.stdin.readline
N = int(input())
route = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(N-1):
    A, B, C = map(int, input().split())
    route[A].append([B, C])
    route[B].append([A, C])
K = int(input())
for _ in range(K):
    D, E = map(int, input().split())
print(route)


'''
11437 LCA 코드 이런 느낌으로 접근해보자
시간 부족.. 꼭 다시 풀어보겠음....
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
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(16, -1, -1):
        if depth[b] - depth[a] >= 2**i:
            b = parent[b][i]
    if a == b:
        print(a)
        continue
    for i in range(16, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    print(parent[a][0])
'''