import heapq

n, m = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())
arr = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

stack = [(0, hx, hy, 0)]
visited = {(0, 0, 0)}
answer = -1

while stack:
    acc, cr, cc, use_wand = heapq.heappop(stack)
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nr, nc = cr + dr, cc + dc
        # 만나자마자 최소일거라는 생각
        if (nr, nc) == (ex, ey):
            answer = acc + 1
            stack = 0
            break
        if 0 < nr <= n and 0 < nc <= m and (nr, nc, use_wand) not in visited:
            if arr[cr][cc] or use_wand:  # 내 자리 1이거나 지팡이 썼으면
                if not arr[nr][nc]:  # 0인 곳만 가기
                    heapq.heappush(stack, (acc + 1, nr, nc, use_wand))
                    visited.add((nr, nc, use_wand))
            else:  # 내 자리 0일 때 완드 써서-> 다 가기
                if arr[nr][nc]:
                    heapq.heappush(stack, (acc + 1, nr, nc, 1))
                    visited.add((nr, nc, 1))
                else:
                    heapq.heappush(stack, (acc + 1, nr, nc, use_wand))
                    visited.add((nr, nc, use_wand))

print(answer)