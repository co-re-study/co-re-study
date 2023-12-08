import sys


def dfs(x):
    global ans
    visited[x] = 1
    team.append(x)
    target = lst[x]
    if visited[target]:
        if target in team:
            ans += team[team.index(target):]
        return
    else:
        dfs(target)


sys.setrecursionlimit(10**6)
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    ans = []
    lst = [0] + list(map(int, input().split()))
    visited = [0]*(N+1)
    for i in range(1, N+1):
        team = []
        dfs(i)
    # print(ans)
    print(N-len(set(ans)))
