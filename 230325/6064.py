# 1 ≤ m, n ≤ 40,000, 1 ≤ x ≤ m, 1 ≤ y ≤ n
# x' = x + 1 m < x이면 x' = 1
# <x':y'>
# <n, m>은 마지막
def check():
    k = x
    while k <= m * n:
        if (k - x) % m == 0 and (k - y) % n == 0:
            return k
        k += m
    return -1


t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())

    print(check())