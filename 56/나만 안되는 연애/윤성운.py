import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
genders = [0] + list(input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    n1, n2, cost = map(int, input().split())
    adj_list[n1].append((n2, cost))
    adj_list[n2].append((n1, cost))

INF = float("inf")
distance = [INF] * (N + 1)
heap = [(0, 1)]
visited = [0] * (N + 1)

while heap:
    cost, current = heapq.heappop(heap)
    visited[current] = 1

    for dest in adj_list[current]:
        if not visited[dest[0]] and dest[1] < distance[dest[0]] and genders[current] != genders[dest[0]]:
            heapq.heappush(heap, (dest[1], dest[0]))
            distance[dest[0]] = dest[1]

for node in range(2, N + 1):
    if distance[node] == INF:
        print(-1)
        break
else:
    print(sum(distance[2:]))