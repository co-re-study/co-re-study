from itertools import combinations

n, m, k = map(int, input().split())
quests = [set(map(int, input().split())) for i in range(m)]
ans = 0
for i in combinations(range(1, 2*n+1), n):
    temp = 0
    for q in quests:
        if q&set(i) == q:
            temp += 1
    ans = max(ans, temp)
print(ans)