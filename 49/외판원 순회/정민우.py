def tsp(now=0, mask=1):
    # 현재 위치가 마지막이고, 처음으로 돌아가는 길이 있는 경우
    if mask == (1 << N) - 1 and matrix[now][0]:
        return matrix[now][0]
    
    # 현재 위치, 방문기록이 일치하는 dp가 있을 경우 저장된 값 리턴
    elif dp[now][mask] != -1:
        return dp[now][mask]

    for destination in range(N):
        # 다음 목적지를 방문한 적이 없고, 현재 위치에서 다음 목적지로 갈 수 있는 경우
        if not mask & (1 << destination) and matrix[now][destination]:
            # 한번도 간적 없으면 한번 돌아봐야됨
            if dp[now][mask] == -1:
                dp[now][mask] = tsp(destination, mask | (1 << destination)) + matrix[now][destination]

            # 간적 있다면 dp랑 비교해봐야됨
            else:
                dp[now][mask] = min(dp[now][mask], tsp(destination, mask | (1 << destination)) + matrix[now][destination])

    # 방문 해봤는데 아무데도 못가더라
    if dp[now][mask] == -1:
        return INF
    
    return dp[now][mask]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
INF = 9999999999999
dp = [[-1] * (1 << N) for _ in range(N)]

print(tsp())
