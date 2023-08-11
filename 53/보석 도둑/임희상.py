import heapq

N, K = map(int, input().split())

jewels = []
bags = []
for _ in range(N):
    heapq.heappush(jewels, list(map(int, input().split())))

for _ in range(K):
    bags.append(int(input()))

bags.sort()

heap = []
answer = 0
for bag in bags:

    while jewels:
        jewel = heapq.heappop(jewels)
        if jewel[0] <= bag:
            heapq.heappush(heap, -jewel[1])
        else:
            heapq.heappush(jewels, jewel)
            break
    
    if heap:
        answer += -heapq.heappop(heap)


print(answer)
