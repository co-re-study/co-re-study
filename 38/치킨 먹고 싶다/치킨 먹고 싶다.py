#매번 c장을 준다
#F장을 모으면 치킨을 공짜로 시킬 수 있다.
# 단골이면 쿠폰으로 시키는 치킨에도 쿠폰이 딸려온다
# 상언이와 두영이 모두 M원을 가지고 있고
# 치킨의 가격은 p원이다.
# 상언이는 두영이보다 치킨을 얼마나 더 시켜먹을 수 있을지


import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    P, M, F, C = map(int, input().split(' '))
    #노단골 치킨
    no_dangol = (M//P) + (M//P*C)//F
    #단골 치킨
    dangol = M // P
    dangol_coupon = M // P * C
    if ( dangol_coupon >= F):
        dangol += (dangol_coupon - F) // (F - C) + 1



    print(dangol - no_dangol)
