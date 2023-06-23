def solution(n, lighthouse):
    
    adj_set = [set() for _ in range(n + 1)]
    for edge in lighthouse:
        adj_set[edge[0]].add(edge[1])
        adj_set[edge[1]].add(edge[0])
    
    # 트리 만들기
    parent = list(range(n + 1))
    stack = [1]
    children_cnt = [0] * (n + 1)
    leaves = []
    while stack:
        current = stack.pop()
        flag = False
        for adj_node in adj_set[current]:
            parent[adj_node] = current
            stack.append(adj_node)
            flag = True
            adj_set[adj_node].remove(current)
            children_cnt[current] += 1
        if not flag:
            leaves.append(current)
    
    # 리프노드부터 내가 안 켜졌으면 부모 등대 켜기
    lighthouses = [0] * (n + 1)
    stack = leaves[:]
    while stack:
        current = stack.pop()
        if not lighthouses[current]:
            lighthouses[parent[current]] = 1
        children_cnt[parent[current]] -= 1
        if parent[current] != 1 and not children_cnt[parent[current]]:
            stack.append(parent[current])
    
    # 켜진 등대 개수 구하기
    answer = 0
    for node in range(1, n + 1):
        if lighthouses[node]:
            answer += 1
            
    return answer