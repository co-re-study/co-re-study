# from collections import deque


# def bfs(N):
#     queue = deque()
#     queue.append(N)
#     visited[N] = 1
#     while queue:
#         node = queue.popleft()
#         for i in graph[node]:
#             if visited[i] == 0:
#                 visited[i] = (visited[node]+1)
#                 queue.append(i)


def dfs(N):
    queue = []
    queue.append(N)
    visited[N] = 1
    while queue:
        node = queue.pop()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = (visited[node]+1)
                queue.append(i)


n = int(input())
a, b = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
dfs(a)
# bfs(a)
print(visited[b]-1)
