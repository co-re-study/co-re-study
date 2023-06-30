N = int(input())
A = sorted(list(set(map(int, input().split()))))
ans = 0
if A == [0]:
    ans = -1
elif A[0]:
    ans = -2
else:
    for a in A:
        if ans != a:
            break
        ans += 1
print(ans+2)