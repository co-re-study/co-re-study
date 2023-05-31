N = int(input())
A = list(map(int, input().split()))
A.sort()
num = 0
for i in range(N):
    # num += sum(A[:i+1])
    num += A[i]*(N-i)
print(num)