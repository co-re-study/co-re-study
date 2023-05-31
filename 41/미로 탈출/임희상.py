import heapq

def solution(n, start, end, roads, traps):
    answer = 0
    trap_set = set(traps)
    adj = [[0]*(n+1) for _ in range(n+1)]
    adj_list = [set() for _ in range(n+1)]
    
    for road in roads:
        departure, destination, dist = road
        if not adj[departure][destination]:
            adj[departure][destination] = dist
            adj_list[departure].add(destination)
            adj_list[destination].add(departure)
        adj[departure][destination] = min(dist, adj[departure][destination])
    
    heap = [(0, start, 0)]
    visited = {}
    
    while heap:
        dist, current, reversed_nodes = heapq.heappop(heap)
        if current == end:
            answer = dist
            break
        if current in visited.keys():
            if reversed_nodes in visited[current].keys():
                continue
            visited[current][reversed_nodes] = dist
        else:
            visited[current] = {reversed_nodes : dist}
        
        if current in trap_set:
            if reversed_nodes & (1<<current):
                reversed_nodes -= (1<<current)
            else:
                reversed_nodes += (1<<current)
        
        for destination in adj_list[current]:
            if bool(reversed_nodes & (1<<current)) ^ bool(reversed_nodes & (1<<destination)):
                if adj[destination][current]:
                    heapq.heappush(heap, (dist+adj[destination][current], destination, reversed_nodes))
            else:
                if adj[current][destination]:
                    heapq.heappush(heap, (dist+adj[current][destination], destination, reversed_nodes))
        
    return answer