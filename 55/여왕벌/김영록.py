import sys
input = sys.stdin.readline
M, N = map(int, input().split())
arr = [1]*(2*M-1)
for _ in range(N):
    z, o, t = map(int, input().split())
    for i in range(z, 2*M-1):
        arr[i] += 1
    for i in range(z+o, 2*M-1):
        arr[i] += 1
for i in range(M):
    print(arr[M-i-1], *arr[M:])
