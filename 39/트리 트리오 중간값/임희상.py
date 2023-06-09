def solution(n, edges):
    answer = 0
    adj = [[] for _ in range(n+1)]
    for edge in edges:
        start, end = edge
        adj[start].append(end)
        adj[end].append(start)
    
    stack = [(1, 0)]
    visited = set()
    root = 0
    root_dist = 0
    while stack:
        current, dist = stack.pop()
        visited.add(current)
        if dist > root_dist:
            root = current
            root_dist = dist
        for destination in adj[current]:
            if destination not in visited:
                stack.append((destination, dist+1))
    
    stack = [(root, 0)]
    root_dists = [0] * (n+1)
    visited = set()
    target = 0
    target_dist = 0
    while stack:
        current, dist = stack.pop()
        visited.add(current)
        root_dists[current] = dist
        if dist > target_dist:
            target = current
            target_dist = dist
        for destination in adj[current]:
            if destination not in visited:
                stack.append((destination, dist+1))
    
    stack = [(target, 0)]
    visited = set()
    while stack:
        current, dist = stack.pop()
        if current != target and current != root:
            if max(dist, root_dists[current]) > answer:
                answer = max(dist, root_dists[current])
        visited.add(current)
        for destination in adj[current]:
            if destination not in visited:
                stack.append((destination, dist+1))
        
    
    return answer