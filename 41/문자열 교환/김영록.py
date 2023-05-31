s = input()
a = s.count('a')
s *= 2
ans = 1000
for i in range(len(s)-a+1):
    ans = min(ans, s[i:i+a].count('b'))
print(ans)

