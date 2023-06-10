import sys
input = sys.stdin.readline

S, C = map(int, input().split())
nums = [int(input()) for _ in range(S)]

left = 0
right = 1000000000

# 파 길이를 다 합해도 C가 안넘으면 모두 라면에 넣기
required = 0
if sum(nums) < C:
    print(sum(nums))
    exit(0)

# 이분탐색
while left <= right:
    middle = (left + right) // 2
    if not middle:
        if right == 1:
            required = 1
        break

    cnt = 0
    for num in nums:
        cnt += num // middle
        if cnt >= C:
            required = middle
            left = middle + 1
            break
    else:
        right = middle - 1

# 라면에 넣을 파 양 계산
answer = 0
cnt = 0
flag = False
for num in nums:
    if not flag:
        cnt += num // required
        if cnt >= C:
            flag = True
            if cnt > C:
                answer += (cnt - C) * required
                continue
        answer += num % required
    else:
        answer += num

print(answer)