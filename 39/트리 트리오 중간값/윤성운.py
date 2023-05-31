def solution(n, edges):
    
    def find_max_distance_node(start_node):
        stack = [(start_node, 0)]
        max_distance = -1
        visited = set()
        while stack:
            current, distance = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            
            if distance > max_distance:
                max_distance = distance
                max_distance_node = current
                is_duplicated = False
            elif distance == max_distance:
                is_duplicated = True
                
            for adj_node in adj_list[current]:
                if adj_node not in visited:
                    stack.append((adj_node, distance + 1))

        return max_distance_node, max_distance, is_duplicated
        
    
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        node1, node2 = edge[0] - 1, edge[1] - 1
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)
        
    # 루트 노드 구하기
    root_node = find_max_distance_node(0)[0]
    
    # 최대 거리의 리프 노드 구하기
    max_distance_leaf_node, max_distance, is_duplicated = find_max_distance_node(root_node)
    if is_duplicated:
        return max_distance
    
    # 최대 거리 구하기
    max_distance, is_duplicated = find_max_distance_node(max_distance_leaf_node)[1:]
    if is_duplicated:
        answer = max_distance
    else:
        answer = max_distance - 1
        
    return answer