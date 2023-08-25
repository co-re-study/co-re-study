import sys
input=sys.stdin.readline


def bellmanford(start, nodes_cnt, edges_cnt):
    for node in range(1, nodes_cnt+1):
        distance[start] = 0
        for j in range(edges_cnt):
            current, next_node, time = edges[j]
            if distance[current] != INF and distance[next_node] > distance[current] + time:
                distance[next_node] = distance[current] + time
                if node == nodes_cnt:
                    return False
    return True


N, M = map(int, input().split())
INF = 1e9
distance = [INF for _ in range(N+1)]

edges = []
for i in range(M):
    edge = list(map(int, input().split()))
    edges.append(edge)

if bellmanford(1, N, M):
    for i in range(2, N+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
else:
    print("-1")


