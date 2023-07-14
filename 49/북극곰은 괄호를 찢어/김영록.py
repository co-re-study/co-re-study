N = int(input())
s = []
ans = 0
for i in input():
    if not len(s) or i == s[-1]:
        s.append(i)
    else:
        s.pop()
    ans = max(ans, len(s))
if len(s):
    print(-1)
else:
    print(ans)
