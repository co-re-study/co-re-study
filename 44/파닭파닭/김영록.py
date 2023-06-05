import sys
input = sys.stdin.readline
S, C = map(int, input().split())
go = [int(input()) for _ in range(S)]
s, e = 1, max(go)
ans = 0
while s <= e:
    cnt = 0
    m = (s+e) // 2
    for g in go:
        cnt += g//m
    if C > cnt:
        e = m-1
    else:
        s = m+1
        ans = m
print(sum(go) - C*ans)
