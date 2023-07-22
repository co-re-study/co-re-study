from itertools import combinations
from collections import defaultdict

def check(a, b, c):
    dist = 0
    for i in range(4):
        if a[i] != b[i]:
            dist += 1
        if b[i] != c[i]:
            dist += 1
        if a[i] != c[i]:
            dist += 1
    return dist

for tc in range(int(input())):
    N = int(input())
    count = defaultdict(int)
    mbti = []
    for now in input().split():
        count[now] += 1
        if count[now] <= 3:
            mbti.append(now)
    ans = 999999999
    for comb in list(combinations(mbti, 3)):
        ans = min(ans, check(*comb))
    print(ans)
    print(mbti)