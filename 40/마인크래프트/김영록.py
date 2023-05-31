'''
0부터 256까지 brute force
'''
import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
A = []
h = 0
ans = 10000000000000000
for _ in range(N):
    A += map(int, input().split())
for i in range(257):
    remove = 0
    stack = 0
    for j in range(N*M):
        if A[j] < i:
            stack += (i-A[j])
        else:
            remove += (A[j]-i)
    inv = remove+B
    if inv < stack:
        continue
    time = 2*remove+stack
    if time <= ans:
        ans = time
        h = i
print(ans, h)