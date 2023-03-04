def solution(sales, links):
    
    # [
    #   현재 노드를 골랐을 때의 최솟값, 
    #   현재 노드를 안 골랐을 때의 최솟값, 
    #   현재 노드를 안 골랐을 때 고른 자식 노드의 골랐을 때의 최솟값, 
    #   현재 노드를 안 골랐을 때 고른 자식 노드의 안 골랐을 때의 최솟값
    # ]
    nodes = [[sales[i], 0, 987654321, 987654321] for i in range(len(sales))]
    parent = [0] * len(sales) # 부모 노드
    child = [0] * len(sales) # 자식 수
    for link in links:
        p, c = link[0] - 1, link[1] - 1
        parent[c] = p
        child[p] += 1
        
    # 리프 노드
    leaves = []
    for i in range(len(nodes)):
        if not child[i]:
            leaves.append(i)
            
    while leaves:
        current = leaves.pop()
        # 루트 노드 도달하면 종료
        if current == 0:
            break

        # 부모 노드의 모든 리프노드를 봤으면 부모 노드도 리프 노드로
        child[parent[current]] -= 1
        if not child[parent[current]]:
            leaves.append(parent[current])
        
        # 부모 노드를 골랐다면 현재 노드의 최솟값만큼 더하기
        nodes[parent[current]][0] += min(nodes[current][:2])
        
        # 현재 노드가 부모 노드의 첫 자식 노드면
        if nodes[parent[current]][2] == 987654321:
            # 부모 노드를 고르지 않았을 때 값은 현재 노드를 골랐을 때의 값으로
            nodes[parent[current]][1] = nodes[current][0]
            nodes[parent[current]][2] = nodes[current][0]
            nodes[parent[current]][3] = nodes[current][1]
            continue
            
        if nodes[parent[current]][2] + min(nodes[current][:2]) <= min(nodes[parent[current]][2:]) + nodes[current][0]:
            nodes[parent[current]][1] += min(nodes[current][:2])
        else:
            nodes[parent[current]][1] += nodes[current][0] - nodes[parent[current]][2] + min(nodes[parent[current]][2:])
            nodes[parent[current]][2] = nodes[current][0]
            nodes[parent[current]][3] = nodes[current][1]
            
    answer = min(nodes[0][:2])
    return answer