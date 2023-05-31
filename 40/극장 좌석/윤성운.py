import sys
input = sys.stdin.readline

# f(n) = f(n-2) + f(n-1)
def find_number_of_cases(num):
    if num in memo:
        return memo[num]
    memo[num - 2] = find_number_of_cases(num - 2)
    memo[num - 1] = find_number_of_cases(num - 1)
    return memo[num - 2] + memo[num - 1]

N = int(input())
M = int(input())
VIP_seats = set()
for _ in range(M):
    VIP_seats.add(int(input()))

# 연속된 좌석 기록
consecutive_seats = []
cnt = 0
for num in range(1, N + 1):
    if num in VIP_seats:
        if cnt != 0:
            consecutive_seats.append(cnt)
        cnt = 0
    else:
        cnt += 1
        if num == N:
            consecutive_seats.append(cnt)

# 연속된 좌석에 대한 값 모두 곱하기
answer = 1
memo = {1: 1, 2: 2}
for num in consecutive_seats:
    if num not in memo:
        memo[num] = find_number_of_cases(num)
    answer *= memo[num]

print(answer)