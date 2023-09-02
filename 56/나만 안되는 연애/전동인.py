import heapq  # 파이썬은 최소힙


def prim(start, graph):
    visited = [0] * (N + 1)
    queue = [(0, start)]
    total_weight = 0

    while queue:
        weight, u = heapq.heappop(queue)
        if visited[u]:
            continue
        visited[u] = 1
        total_weight += weight

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(queue, (w, v))

    if all(visited[1:]):
        return total_weight
    return -1


N, M = map(int, input().split())
uni = [''] + list(input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    if uni[u] != uni[v]:
        graph[u].append((v, w))
        graph[v].append((u, w))

print(prim(1, graph))
