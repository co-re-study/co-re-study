# 그냥 방문하는 노드마다 거리 한 번씩 재보면 되지 않을까..
# DFS 두 번이면 되지 않을까..? => 아아아아니 반례도 맞았는데 왜 틀려어어엉어어어어어어어어어
def dfs(depth, distance):
    global N, D
    if depth == N:
        return

    else:
        for idx in adj[depth]:
            if distance + 1 <= D and idx not in visit:
                visit.add(idx)
                dfs(idx, distance + 1)
        return


N, M, D = map(int, input().split(" "))
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

queue = [[M, 0]]
visited = set()
visit = set()
ans = M * 2
dfs(M, 0)
flag = True
for j in range(1, N + 1):
    if j not in visit:
        flag = False

if not flag:
    while queue:
        node, cnt = queue.pop()
        visited.add(node)
        for i in adj[node]:
            if i not in visited:
                queue.append([i, cnt + 1])
                dfs(i, 0)

                check = True
                for j in range(1, N+1):
                    if j not in visit:
                        check = False
                        break
                if check:
                    flag = True
            if flag:
                ans = (cnt + 1) * 2
                break

        if flag:
            break
else:
    ans = 0
print(ans)