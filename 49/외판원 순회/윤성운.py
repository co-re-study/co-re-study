import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 열: 현재 노드, 행: 방문한 도시들
dp = [[0] * (N) for _ in range(1 << N)]

# 0번 도시부터 출발한다고 가정
for i in range(1, N):
    dp[(1 << i) + 1][i] = arr[0][i]

for i in range(3, 1 << N):
    # 0번 도시를 안 밟은 경우면 continue
    if not i & 1:
        continue
    for j in range(1, N):
        #  j번 도시를 마지막으로 밟은 경우만 보기
        if not i & (1 << j):
            continue
        
        # 현재 방문한 도시 중 0번 도시와 j번 도시를 제외한 도시들: k번 도시
        # 0번 도시 -> k번 도시 -> j번 도시로 가는 가장 적은 비용 고르기
        min_num = 987654321
        for k in range(1, N):
            if not i & (1 << k) or j == k or not arr[k][j] or not dp[(i ^ (1 << j))][k]:
                continue
            min_num = min(dp[(i ^ (1 << j))][k] + arr[k][j], min_num)

        if min_num != 987654321:
            dp[i][j] = min_num

# 마지막으로 다시 0번 도시로 왔을 때 비용 더해서 최소 비용 구하기
answer = 987654321
for i in range(1, N):
    if not arr[i][0] or not dp[-1][i]:
        continue
    answer = min(dp[-1][i] + arr[i][0], answer)

print(answer)