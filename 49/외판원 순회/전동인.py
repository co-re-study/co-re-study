n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(1 << n) for _ in range(n)]


def TSP(start, visited):
    if visited == (1 << n) - 1:  # 모든 경유지를 방문 했다면, 돌아가는 비용을 리턴
        return dist[start][0] if dist[start][0] > 0 else 1000000*n

    if dp[start][visited] != 0:  # start에서 visited 까지의 최소값이 존재한다면, 해당 비용을 리턴
        return dp[start][visited]

    dp[start][visited] = 1000000*n  # 해당 경우에 대해 처음 계산하는 경우, 최대값을 할당

    for i in range(1, n):  # 이동 가능한 경로 탐색
        # i 도시를 방문하지 않았고 방문할 수 있다면
        if not (visited >> i) % 2 and dist[start][i]:
            dp[start][visited] = min(dp[start][visited], TSP(
                i, visited | (1 << i)) + dist[start][i])  # i에서 i를 포함한 visited를 경유하는 경우중 최솟값 + start->i 비용

    return dp[start][visited]


print(TSP(0, 1))
