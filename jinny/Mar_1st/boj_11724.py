n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

answer = 0
for i in range(n+1):
    if not visited[i]:
        stack = [i]
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = 1
            stack += adj[node]
        else:
            answer += 1
print(answer - 1)
