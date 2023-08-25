N, M = map(int, input().split())
edges = []

for _ in range(M):
    edges.append(list(map(int, input().split())))

dists = [float('INF')] * (N+1)
dists[1] = 0

for i in range(N):

    for edge in edges:
        current, post, cost = edge
        if dists[current] != float('INF') and dists[post] > dists[current] + cost:
            dists[post] = dists[current] + cost
    
for edge in edges:
    current, post, cost = edge
    if dists[current] != float('INF') and dists[post] > dists[current] + cost:
        print("-1")
        break
else:
    for i in range(2, N+1):
        if dists[i] == float("inf"):
            print(-1)
        else:
            print(dists[i])