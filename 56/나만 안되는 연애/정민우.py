# 주어진 조건 만족하는 MST의 거리 합 구하기

from heapq import heapify, heappop, heappush

N, M = map(int, input().split())
univs = list(map(lambda x: [x, []], input().split()))

for _ in range(M):
    u, v, d = map(int, input().split())
    u, v = u - 1, v - 1
    # 남남, 여여 학교로 가는 경로 제거
    if univs[u][0] != univs[v][0]:
        univs[u][1].append((d, u, v))
        univs[v][1].append((d, v, u))

# 0번부터 프림으로 탐색하기
visited, ans = {0}, 0
heap = univs[0][1]
heapify(heap)
while heap:
    d, u, v = heappop(heap)
    if v not in visited:
        visited.add(v)
        for edge in univs[v][1]:
            if edge[2] not in visited:
                heappush(heap, edge)
        ans += d
        # 다 방문하면 총 거리 출력 후 종료
        if len(visited) == N:
            print(ans)
            exit(0)

# 다 방문하지 못했을 경우 -1 출력
print(-1)