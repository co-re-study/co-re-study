# solution(n, width): 열의 개수가 width개이고 n개의 카드를 골라야 할 떄 포카드가 나오는 모든 경우의 수
# ex) N = 14

# 1. 포카드가 하나만 나온 경우
# 13개의 열 중에 1개의 열만 포카드(카드 4개 소모)이고, 나머지 12개 열에서 10개를 골랐을 때 모두 포카드가 아니어야 함
# 13C1 * (12개의 열에서 10개를 고른 경우 - 12개의 열에서 10개를 골랐을 때 포카드가 나온 모든 경우)
# 13C1 * (48C10 - solution(10, 12))

# 2. 포카드가 두 개 나온 경우
# 13개의 열 중에 2개의 열만 포카드(카드 8개 소모)이고, 나머지 11개 열에서 6개를 골랐을 때 모두 포카드가 아니어야 함
# 13C2 * (11개의 열에서 6개를 고른 경우 - 11개의 열에서 6개를 골랐을 때 포카드가 나온 모든 경우)
# 13C2 * (44C6 - solution(6, 11))

# 3. 포카드가 세 개 나온 경우
# 13개의 열 중에 3개의 열만 포카드(카드 12개 소모)이고, 나머지 10개 열에서 2개를 고르기
# 13C3 * 10개의 열에서 2개를 고른 경우
# 13C2 * 40C2

import sys
input = sys.stdin.readline

# 재귀함수
def solution(n, width):
    if n < 4:
        return 0
    if n == 4:
        return width
    acc = 0
    cnt = 1
    while n >= 4:
        n -= 4
        if not n:
            acc += comb(width, cnt)
        else:
            acc += comb(width, cnt) * (comb((width - cnt) * 4, n) - solution(n, width - cnt))
        cnt += 1
    return acc % 10007


# nCr
def comb(n, r):
    num = 1
    for i in range(r):
        num *= (n - i)
    for i in range(1, r + 1):
        num //= i
    return num


N = int(input())
print(solution(N, 13))