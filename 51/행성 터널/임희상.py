import heapq

N = int(input())
coordinates = []
for i in range(N):
    coordinates.append(list(map(int, input().split())) + [i])

x_order = sorted(coordinates, key=lambda x: x[0])
y_order = sorted(coordinates, key=lambda x: x[1])
z_order = sorted(coordinates, key=lambda x: x[2])


adj = [[] for _ in range(N)]
for i in range(N-1):
    dist, start, end = abs(x_order[i+1][0]-x_order[i][0]), x_order[i][3], x_order[i+1][3]
    adj[start].append((dist, end))
    adj[end].append((dist, start))
    
for i in range(N-1):
    dist, start, end = abs(y_order[i+1][1]-y_order[i][1]), y_order[i][3], y_order[i+1][3]
    adj[start].append((dist, end))
    adj[end].append((dist, start))
    
for i in range(N-1):
    dist, start, end = abs(z_order[i+1][2]-z_order[i][2]), z_order[i][3], z_order[i+1][3]
    adj[start].append((dist, end))
    adj[end].append((dist, start))


visited = {0}
heap = list(adj[0])
heapq.heapify(heap)

answer = 0
while heap:
    distance, destination = heapq.heappop(heap)
    if destination in visited:
        continue
    visited.add(destination)
    answer += distance
    for edge in adj[destination]:
        if edge[1] not in visited:
            heapq.heappush(heap, edge)

print(answer)