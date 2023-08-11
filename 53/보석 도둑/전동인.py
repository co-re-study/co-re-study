import heapq

# 입력 받기
N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]  # [[무게, 가격]]
bags = [int(input()) for _ in range(K)]

# 보석과 가방을 무게를 기준으로 오름차순 정렬
jewels.sort(key=lambda x: x[0])
bags.sort()


def push_q(priority_q, value):
    # 최대 힙을 위해 음수화
    heapq.heappush(priority_q, -value)


def pop_q(priority_q):
    # 최대 힙을 위해 음수화
    return -heapq.heappop(priority_q)


value_q = []  # 최대 힙(비싼 순서)
index = 0
answer = 0

for bag in bags:
    # 해당 가방에 담을 수 있는 보석들을 우선순위 큐에 넣는다
    while index < N and jewels[index][0] <= bag:
        push_q(value_q, jewels[index][1])
        index += 1

    # 가장 가치가 높은 보석을 선택
    if value_q:
        answer += pop_q(value_q)

print(answer)
