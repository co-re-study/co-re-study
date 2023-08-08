import sys, heapq
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for i in range(K)]

jewels = deque(sorted(jewels, key=lambda x: (x[0], -x[1]))) # 보석은 무게 오름차순, 같은 무게면 가격 내림차순으로 정렬
bags.sort() # 가방은 오름차순으로 정렬

heap = [] # 보석 넣을 곳
answer = 0
for bag in bags:
    # 현재 가방이 담을 수 있는 모든 보석을 힙에 넣기
    while jewels:
        # 가장 작은 무게의 보석이 현재 가방이 담을 수 있는 무게 이하면 heap에 넣기
        if jewels[0][0] <= bag:
            heapq.heappush(heap, -jewels.popleft()[1])
        else:
            break
    # 힙에 보석이 들어있다면 가장 무게 큰 보석 누적
    if heap:
        answer -= heapq.heappop(heap)

print(answer)