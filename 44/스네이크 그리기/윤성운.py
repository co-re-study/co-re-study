# n, m 중 하나라도 짝수인 경우
# (가로가 짝수라고 가정)
# → → → → ... ↓
# ↑       ↓ ← ↓
# ↑       ↓ . ↓
# ↑       . . .
# ↑       . . .
# ↑       . ↑ .
# ↑ ← ... ← ↑ ← 

# n, m이 모두 홀수인 경우
# → → → → → ... ↓
# ↑ ↓ ... ← ← ← ←
# ↑ → → → → ... ↓
# ↑             ←
# ↑      .       
# ↑      .       
# ↑      .       
# ↑ → → → → ... ↓
# ↑ ←  ...  ↓ ← ↓
#   ↑ ←   ↑ ← ↑ ← 

import sys
input = sys.stdin.readline

# x, y에 맞게 출력
def auto_print(num1, num2, is_num1_x):
    if is_num1_x:
        print(f"{num1} {num2}")
    else:
        print(f"{num2} {num1}")


# n, m 중 하나라도 짝수인 경우
def make_even_snake(even_num, odd_num, is_even_num_x):
    # 모든 칸을 지날 수 있음
    print(even_num * odd_num)

    for i in range(1, even_num + 1):
        auto_print(i, 1, is_even_num_x)

    for i in range(even_num, 0, -1):
        for j in range(2, odd_num + 1):
            if not i % 2:
                auto_print(i, j, is_even_num_x)
            else:
                auto_print(i, odd_num - j + 2, is_even_num_x)


# n, m이 모두 홀수인 경우
def make_odd_snake(n, m):
    # 한 칸 빼고 나머지 모두 지날 수 있음
    print(n * m - 1)

    for x in range(1, n + 1):
        print(f"{x} 1")

    for y in range(2, m - 1):
        for x in range(2, n + 1):
            if not y % 2:
                print(f"{n - x + 2} {y}")
            else:
                print(f"{x} {y}")

    for x in range(n, 1, -1):
        for y in range(2):
            if x % 2:
                print(f"{x} {m - 1 + y}")
            else:
                print(f"{x} {m - y}")

    for y in range(m - 1, 1, -1):
        print(f"1 {y}")


n, m = map(int, input().split())

if not n % 2:
    make_even_snake(n, m, True)
elif not m % 2:
    make_even_snake(m, n, False)
else:
    make_odd_snake(n, m)
