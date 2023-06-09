def solution(n, path, order):
    
    adj_list = [[] for _ in range(n)]
    
    for nodes in path:
        adj_list[nodes[0]].append(nodes[1])
        adj_list[nodes[1]].append(nodes[0])
        
    waiting_nodes = set() # 아직 갈 수 없는 노드
    nodes_dict = dict() # key: 먼저 방문해야 하는 노드, value: 이후 방문할 노드
    for nodes in order:
        nodes_dict[nodes[0]] = nodes[1]
        waiting_nodes.add(nodes[1])
        
    stack = [0]
    visited = set()
    answer = True
    
    # 0이 waiting_nodes에 있으면 시작조차 불가
    if 0 in waiting_nodes:
        stack = []
        
    while stack:
        current = stack.pop()
        if current in visited:
            continue
            
        # 현재 노드를 방문해야 방문할 수 있는 노드가 있다면,
        if current in nodes_dict:
            next_node = nodes_dict[current]
            # 다음 노드에 도달했었다면 스택에 추가
            if nodes_dict[current] not in waiting_nodes:
                stack.append(next_node)
            # 아직 도달하지 못했다면 다음에 도달할 때 방문하도록
            else:
                waiting_nodes.remove(next_node)
            
        visited.add(current)
        
        for destination in adj_list[current]:
            if destination not in visited:
                # 도달했지만 아직 방문할 수 없는 노드라면 다음에 만날 때 방문
                if destination in waiting_nodes:
                    waiting_nodes.remove(destination)
                # 방문할 수 있는 노드면 스택에 추가
                else:
                    stack.append(destination)
        
    if len(visited) < n:
        answer = False
        
    return answer