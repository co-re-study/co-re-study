from collections import deque
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]  # 문자
dp = [[[987654321, 987654321, 987665321] for _ in range(m)] for _ in range(n)]

for man in range(3):
    r, c = map(lambda x: int(x) - 1, input().split())
    q = deque([(r, c, 1)])
    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    dp[r][c][man] = 0
    while q:
        cr, cc, acc = q.popleft()
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == '0' and visited[nr][nc] == 0:
                dp[nr][nc][man] = acc
                q.append((nr, nc, acc + 1))
                visited[nr][nc] = 1
answer = 987654321
result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '0':
            mx = max(dp[i][j])
            if mx < answer:
                answer = mx
                result = 1
            elif mx == answer:
                result += 1
if answer == 987654321:
    print(-1)
else:
    print(answer)
    print(result)