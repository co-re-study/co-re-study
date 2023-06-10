import sys

S, C = map(int, input().split())
right = 0
left = 1
spring_onions = []
total = 0

for _ in range(S):
    length = int(sys.stdin.readline())
    spring_onions.append(length)
    total += length
    right = max(right, length)


def determine(target):

    chickens = 0
    for spring_onion in spring_onions:
        chickens += spring_onion // target
    
    return chickens

prev = left
answer = 0
while left <= right:  # 종료 조건 주의
    mid = (right + left) // 2
    if mid == prev:
        break
    chickens = determine(mid)
    if chickens >= C:
        left = mid + 1
        answer = total - C*mid
    else:
        right = mid - 1
    prev = mid


print(answer)