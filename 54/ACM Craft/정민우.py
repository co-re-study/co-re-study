def time(n):
    if not graph[n]:
        times[n] = D[n]
        return D[n]

    for node in graph[n]:
        if times[node] == -1:
            times[n] = max(times[n], D[n] + time(node))
        else:
            times[n] = max(times[n], D[n] + times[node])
    return times[n]


for tc in range(int(input())):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    times = [-1] * N
    graph = [[] for _ in range(N)]
    for k in range(K):
        x, y = map(lambda x: int(x) - 1, input().split())
        graph[y].append(x)
    W = int(input()) - 1

    print(time(W))
