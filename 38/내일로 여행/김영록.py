import sys

input = sys.stdin.readline
INF = sys.maxsize
N, R = map(int, input().split())
cities = {}
idx = 0
for city in list(input().split()):
    cities[city] = idx
    idx += 1
graph = [[INF]*N for _ in range(N)]
ticket_graph = [[INF]*N for _ in range(N)]
M = int(input())
travel = list(input().split())
K = int(input())
for _ in range(K):
    t, s, e, cost = input().split()
    cost = int(cost)
    s = cities[s]
    e = cities[e]
    if t in ['Mugunghwa', 'ITX-Saemaeul', 'ITX-Cheongchun']:
        ticket_graph[s][e] = 0
        ticket_graph[e][s] = 0
    elif t in ['S-Train', 'V_Train']:
        ticket_graph[s][e] = min(ticket_graph[s][e], cost/2)
        ticket_graph[e][s] = min(ticket_graph[s][e], cost/2)
    else:
        ticket_graph[s][e] = min(ticket_graph[s][e], cost)
        ticket_graph[e][s] = min(ticket_graph[s][e], cost)
    graph[s][e] = min(graph[s][e], cost)
    graph[e][s] = min(graph[s][e], cost)
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
            if ticket_graph[i][j] > ticket_graph[i][k] + ticket_graph[k][j]:
                ticket_graph[i][j] = ticket_graph[i][k] + ticket_graph[k][j]
cost = 0
ticket_cost = R
for i in range(M-1):
    l, r = cities[travel[i]], cities[travel[i+1]]
    cost += graph[l][r]
    ticket_cost += ticket_graph[l][r]
if cost - ticket_cost > 0:
    print('Yes')
else:
    print('No')
