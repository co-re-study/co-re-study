def floyd_warshall(n, adj):
    # 모든 노드로부터 모든 노드로의 거리
    dists = [[float('INF')] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                dists[i][j] = 0
            else:
                dists[i][j] = adj[i][j]

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dists[i][j] = dists[j][i] = min(dists[i][j], dists[i][k] + dists[k][j])

    return dists


def solution(n, s, a, b, fares):
    answer = 0
    adj = [[float('INF')]*(n+1) for _ in range(n+1)]
    for fare in fares:
        start, end, dist = fare
        adj[start][end] = adj[end][start] = dist
    print(adj)
    dists = floyd_warshall(n, adj)

    for i in range(1, n+1):
        print(dists[i])

    answer = float('INF')
    for i in range(1, n+1):
        answer = min(answer, dists[s][i] + dists[i][a]+ dists[i][b])

    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
