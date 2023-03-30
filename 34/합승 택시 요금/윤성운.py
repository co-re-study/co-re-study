import heapq

def solution(n, s, a, b, fares):
    
    # 다익스트라
    def dijk(start, distance):
        distance[start] = 0
        heap = [(0, start)]
        visited = set()
        
        while heap:
            dist, current = heapq.heappop(heap)
            if current in visited:
                continue
            for destination_info in adj_list[current]:
                destination, cost = destination_info
                if distance[current] + cost < distance[destination]:
                    distance[destination] = distance[current] + cost
                    heapq.heappush(heap, (distance[destination], destination))
    
    adj_list = [[] for _ in range(n + 1)]
    INF = 987654321
    distance_A = [INF] * (n + 1)
    distance_B = [INF] * (n + 1)
    distance_total = [INF] * (n + 1)
    
    for fare in fares:
        adj_list[fare[0]].append((fare[1], fare[2]))
        adj_list[fare[1]].append((fare[0], fare[2]))
                    
    dijk(a, distance_A) # A에서 각 노드까지의 최소 가중치 구하기
    dijk(b, distance_B) # B에서 각 노드까지의 최소 가중치 구하기
    dijk(s, distance_total) # S에서 각 노드까지의 최소 가중치 구하기
    answer = INF
    
    # node: A와 B가 헤어질 노드
    for node in range(1, n + 1):
        # 함께 간 거리 + A 혼자 간 거리 + B 혼자 간 거리
        distance = distance_total[node] + distance_A[node] + distance_B[node]
        if distance < answer:
            answer = distance

    return answer