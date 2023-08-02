n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

gone = []
# 사라질 섬 찾기
for i in range(n):
    if 'X' in arr[i]:
        for j in range(m):
            if arr[i][j] == 'X':
                island = 0  # 범위 밖도 바다니까 그냥 섬을 셀게
                for dr, dc in ((1, 0), (0, 1), (0, -1), (-1, 0)):
                    if 0 <= i + dr < n and 0 <= j + dc < m:
                        if arr[i + dr][j + dc] == 'X':
                            if island:
                                break
                            island += 1
                else:
                    gone.append((i, j))
# 섬 사라지기
for cr, cc in gone:
    arr[cr][cc] = '.'

# 지도 범위 찾기
r1, r2 = 99, 0
c1, c2 = 99, 0
for i in range(n):
    if 'X' in arr[i]:
        r1 = min(r1, i)
        r2 = max(r2, i)
        for j in range(m):
            if arr[i][j] == 'X':
                c1 = min(c1, j)
                c2 = max(c2, j)
# 출력
for i in range(r2 - r1 + 1):
    print(*arr[r1 + i][c1:c2+1], sep='')