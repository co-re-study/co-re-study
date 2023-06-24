from collections import deque


def solution(n, lighthouse):
    routes = [[] for _ in range(n+1)]
    answer = 0
    for s, e in lighthouse:
        routes[s].append(e)
        routes[e].append(s)
    visited = [0]*(n+1)
    queue = deque()
    for i in range(1, n+1):
        if len(routes[i]) == 1:
            queue.append(i)
    while queue:
        current = queue.popleft()
        if not routes[current]:
            break
        next_node = routes[current][0]
        routes[current] = []
        routes[next_node].remove(current)
        if len(routes[next_node]) == 1:
            queue.append(next_node)
        if visited[current] == 1:
            continue
        visited[next_node] = 1
    return sum(visited)


print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
