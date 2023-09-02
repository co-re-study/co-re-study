import heapq

N, M = map(int, input().split())

schools = [0] + input().split()
adj = [[] for _ in range(N+1)]
heap = []

for _ in range(M):
    u, v, d = map(int, input().split())
    if schools[u] == schools[v]:
        continue
    adj[u].append((v, d))
    adj[v].append((u, d))
    if u == 1:
        heapq.heappush(heap, (d, v))
    if v == 1:
        heapq.heappush(heap, (d, u))

visited = {1}
answer = 0
while heap:
    current_dist, current = heapq.heappop(heap)
    if current in visited:
        continue
    visited.add(current)
    answer += current_dist

    for destination, dist in adj[current]:
        if destination not in visited:
            heapq.heappush(heap, (dist, destination))

if len(visited) == N:
    print(answer)
else:
    print(-1)