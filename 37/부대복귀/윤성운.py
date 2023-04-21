import heapq

def solution(n, roads, sources, destination):
    
    def dijk(start):
        queue = [(0, start)]
        distance[start] = 0
        
        while queue:
            cost, current_node = heapq.heappop(queue)
            if cost > distance[current_node]:
                continue
            
            for adj_node in adj_list[current_node]:
                if cost + 1 < distance[adj_node]:
                    distance[adj_node] = cost + 1
                    heapq.heappush(queue, (cost + 1, adj_node))
    
    INF = 987654321
    adj_list = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    
    # 인접 리스트 생성
    for road in roads:
        adj_list[road[0]].append(road[1])
        adj_list[road[1]].append(road[0])
    
    # 부대에서부터 모든 노드까지 최소 거리 구하기
    dijk(destination)

    # 각 출발지에서 부대까지 거리 구하기
    answer = []
    for source in sources:
        if distance[source] == INF:
            answer.append(-1)
        else:
            answer.append(distance[source])
        
    return answer