# 목표. 주어진 리스트에서 중복되지 않는 수열을 갖는 경우의 수
N = int(input())
numbers = list(map(int, input().split()))

count = {}  # 중복 카운트를 위한 딕셔너리
left = 0
right = 0
answer = 0

while left < N:
    # 중복이 없을 때까지, 오른쪽 포인터를 이동
    while right < N and count.get(numbers[right], 0) < 1:
        count[numbers[right]] = count.get(numbers[right], 0) + 1
        right += 1
    # 중복이 발생했다면, 왼쪽 포인터를 이동하여 경우의 수 산출
    answer += (right - left)  # 해당 범위에서 (right - left)만큼 경우가 발생한다.
    count[numbers[left]] -= 1
    left += 1

print(answer)
