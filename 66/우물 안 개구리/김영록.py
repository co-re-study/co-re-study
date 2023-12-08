import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [0]+list(map(int, input().split()))
member = [set() for i in range(N+1)]
ans = 0
for i in range(M):
    A, B = map(int, input().split())
    member[A].add(B)
    member[B].add(A)
for i in range(1, N+1):
    for j in member[i]:
        if arr[i] <= arr[j]:
            break
    else:
        ans += 1
print(ans)
