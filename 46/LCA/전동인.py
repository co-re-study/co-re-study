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


# 시간 초과 -----------------------------------------------
# 부모 목록 조회
def find(x):
    par_seq = [x]
    while x != parents[x]:
        x = parents[x]
        par_seq.append(x)
    return par_seq


n = int(input())
graph = [[] for _ in range(n+1)]
parents = [0] * (n+1)

# graph
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS로 트리 그리기
visited = [0] * (n+1)
stack = [(1, 1)]  # start, parent

while stack:
    start, parent = stack.pop()
    visited[start] = 1
    parents[start] = parent
    for i in graph[start]:
        if not visited[i]:
            stack.append((i, start))
            graph[i].remove(start)

m = int(input())
for _ in range(m):
    c, d = map(int, input().split())

    # 부모 리스트
    c_par = find(c)
    d_par = find(d)

    flag = False
    for j in c_par:
        for k in d_par:
            if j == k:
                print(j)
                flag = True
                break
        if flag:
            break
