import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
T = int(input())
answer = [0 for x in range(T)]
for tc in range(T):
    P, M, F, C = map(int,input().split())
    temp = M//P*C
    ccnt = temp%F + (temp//F)*C - F
    answer[tc] = (1+ccnt//(F-C) if ccnt > 0 else 0) if ccnt else 1
print(*answer, sep='\n')
