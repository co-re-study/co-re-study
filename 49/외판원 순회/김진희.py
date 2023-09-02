def sales(x, visited):
    # 마지막 행성에선 x -> 0으로 가는 비용 반환
    if visited == (1 << n) - 1:
        # 길이 0이면 INF 반환 잊지 말자
        if arr[x][0]:
            return arr[x][0]
        else:
            return INF
    # 계산 완료인 곳 반환   -> dp가 초기값이 INF면 완료라 INF인지 INF라 INF인지 구분이 안 된다?
    if dp[x][visited] != -1:
        return dp[x][visited]
    # 일단 방문했으니까 -1을 INF로 방문 체크 해주는 건가봐..
    dp[x][visited] = INF
    # 전체 행성 방문
    for i in range(1, n):
        # 길이 없는 곳 pass or 이미 방문한 곳 제외
        if not arr[x][i] or visited & (1 << i):
            continue
        # 다음 행선지 순회 비용 중 가장 짧은 곳 기록 (i번 행성, visited에 i찍고) 방문 하지 않은 곳 비용 + i 비용
        dp[x][visited] = min(dp[x][visited], sales(i, visited | (1 << i)) + arr[x][i])

    return dp[x][visited]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
dp = [[-1] * (1 << n) for _ in range(n)]  # r : i번 행성 / c: 0101번 방문기록부터 뒤로 몇 더 가야하나 (방문하지 않은 곳의 최소값)
print(sales(0, 1))