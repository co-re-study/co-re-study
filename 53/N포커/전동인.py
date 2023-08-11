import math

N = int(input())
mod = 10007


def comb(n, r):
    # 조합 연산 (nCr)
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


if N < 4:
    print(0)
elif N == 4:
    print(13)
elif N == 52:
    print(1)
else:
    total = 0

    n = N // 4
    # 중복된 조합을 제거/추가
    for i in range(1, n+1):
        sign = (-1)**(i+1)
        total += sign * comb(13, i) * comb(52 - (4*i), N - (4*i))

    print(total % mod)
