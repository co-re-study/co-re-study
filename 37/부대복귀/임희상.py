from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    adj = [set() for _ in range(n+1)]
    dists = [-1] * (n+1)
    for road in roads:
        start, end = road
        adj[start].add(end)
        adj[end].add(start)
    
    queue = deque([[destination, 0]])
    visited = set()
    while queue:
        current, dist = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        dists[current] = dist
        for next_destination in adj[current]:
            if next_destination not in visited:
                queue.append([next_destination, dist+1])
    
    for source in sources:
        answer.append(dists[source])
    
    return answer