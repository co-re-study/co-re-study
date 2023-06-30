def solution(n, lighthouse):
    answer = 0
    adj = [[] for _ in range(n+1)]
    parents = [0] * (n+1)
    children = [set() for _ in range(n+1)]
    
    for edge in lighthouse:
        start, end = edge
        adj[start].append(end)
        adj[end].append(start)
    
    stack = [1]
    visited = set()
    leaves = set()
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        flag = False
        for destination in adj[current]:
            if destination not in visited:
                parents[destination] = current
                children[current].add(destination)
                stack.append(destination)
                flag = True
        if not flag:
            leaves.add(current)
            
    dp = [[1, 0] for _ in range(n+1)]  # [나 켜짐, 나 안 켜짐]
    
    stack = list(leaves)
    visited = set()
    while stack:
        current = stack.pop()
        if current == 1:
            continue
        dp[parents[current]][0] += min(dp[current])
        dp[parents[current]][1] += dp[current][0]
        visited.add(current)
        for child in children[parents[current]]:
            if child not in visited:
                break
        else:
            stack.append(parents[current])
            
    answer = min(dp[1])
    return answer