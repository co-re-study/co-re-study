'''
쿠폰c장 줌 쿠폰f장 모으면 치킨 공짜
상언 두영 m원 치킨 p원
'''
import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    P, M, F, C = map(int, input().split())
    d_Ch = s_Ch = M//P
    # s_Ch = M//P
    d_Co = s_Co = M//P*C
    # s_Co = M//P*C
    d_Ch += d_Co//F
    while s_Co // F > 0:
        s_Ch += (s_Co-F)//(F-C) + 1
        s_Co -= s_Co*(F-C)
    print(s_Ch-d_Ch)
