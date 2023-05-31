from collections import deque
def solution(n, path, order):
    # 노드들을 큐에 넣으며 방문처리를 하고 모두 방문할 수 있을지를 판단하는 문제
    # 일반 그래프로도 풀 수 있겠지만 트리의 루트에서 시작한다는 말이 있으니
    # 부모노드가 선행노드가 되는 생각으로 트리를 구성했음.
    
    # 노드를 큐에 넣는 상황은 두 개
    # 1. 방문한 노드의 자식 노드
    # 2. 문제에서 선후관계로 연결되어 선행노드를 방문했을 때 방문 가능해지는 노드
    # 2번 상황은 이미 그 부모를 방문했을 것.
    
    # 큐에서 꺼낸 노드의 선행 노드를 확인하고 방문했다면 이 노드도 방문처리 한다.
    answer = True
    left = n
    req_dict = {}
    next_dict = {}
    adj = [[] for _ in range(left)]
    for edge in path:
        start, end = edge
        adj[start].append(end)
        adj[end].append(start)
    visited = set()
    queue = deque([0])
    parents = {}
    while queue:  # 트리 만들기
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        for destination in adj[current]:
            if destination not in visited:
                parents[destination] = current
                queue.append(destination)
                
    for req in order:
        prev, after = req
        req_dict[after] = prev
        next_dict[prev] = after
    queue = deque([0])
    visited = set()
    
    while queue:
        current = queue.popleft()
        if current in req_dict.keys():
            if req_dict[current] not in visited:
                continue
        if current in visited:
            continue
        visited.add(current)
        left -= 1
        for destination in adj[current]:
            if destination not in visited:
                queue.append(destination)
        if current in next_dict.keys():
            if parents[next_dict[current]] in visited:
                queue.append(next_dict[current])
        
    if left:
        answer = False
    return answer