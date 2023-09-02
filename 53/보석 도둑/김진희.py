import heapq

n, k = map(int, input().split())
diamonds = []  # 무게, 가격
for i in range(n):
    m, v = map(int, input().split())
    diamonds.append((m, v))  # 무게, 가격
# 이거랑 힙푸시로 넣는 거랑 비교해볼래 소트도
heapq.heapify(diamonds)
bags = list(int(input()) for _ in range(k))
bags.sort()

answer = 0
q = []
# 가방을 돌면서
for bag in bags:
    # 나보다 작은걸 다 q에 넣어둔다
    while diamonds and diamonds[0][0] <= bag:
        heapq.heappush(q, -heapq.heappop(diamonds)[1])
    if q:
        # q중 제일 비싼 것만 뽑는다
        answer -= heapq.heappop(q)
    elif not diamonds:  # 보석이 더이상 없으면 끝
        break

print(answer)