n = int(input())
graph = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]  # 부모
depth = [0 for _ in range(n+1)]  # 노드 깊이

# graph
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS, 부모와 노드 깊이 구하기
visited = [0 for _ in range(n+1)]
stack = [(1, 0)]  # start, depth
while stack:
    node, d = stack.pop()
    visited[node] = 1
    depth[node] = d
    for next_node in graph[node]:
        if not visited[next_node]:
            parents[next_node] = node
            stack.append((next_node, d+1))

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    if depth[a] < depth[b]:  # a를 depth가 큰 녀석으로
        a, b = b, a
    while depth[a] != depth[b]:  # 깊이를 동일하게 만듬
        a = parents[a]
    while a != b:  # 같이 부모 찾음
        a = parents[a]
        b = parents[b]
    print(a)
