# 유기농 배추
T = int(input())
for tc in range(T):
    m, n, k = map(int, input().split())  # 가로, 세로, 배추 수
    arr = [[0]*m for _ in range(n)]
    # print(arr)
    for cabbage in range(k):
        r, c = map(int, input().split())
        arr[c][r] = 1
    answer = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                arr[i][j] = 0
                answer += 1
                stack = [(i, j)]
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc]:
                            stack.append((nr, nc))
                            arr[nr][nc] = 0
    print(answer)