# import sys
# from collections import defaultdict


# def find_root(x):
#     if x != roots[x]:
#         roots[x] = find_root(roots[x])
#     return roots[x]


# input = sys.stdin.readline
# N, M, K = map(int, input().split())
# candies = [0]+list(map(int, input().split()))
# roots = [i for i in range(N+1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     s, e = min(find_root(a), find_root(b)), max(find_root(a), find_root(b))
#     roots[e] = s
# groups_dict = defaultdict(lambda: [0, 0])
# for i in range(1, N+1):
#     groups_dict[roots[i]][0] += 1
#     groups_dict[roots[i]][1] += candies[i]
# groups_info = [i for i in groups_dict.values()]
# groups_info.sort()
# l = len(groups_info)
# dp = [[0]*K for _ in range(l+1)]
# for i in range(1, l+1):
#     weight, value = groups_info[i-1]
#     for j in range(1, K):
#         if j <= weight:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
# print(dp[l-1][K-1])


import sys
from collections import deque


def bfs(x):
    group = [1, candies[x]]
    queue = deque()
    queue.append(x)
    visited[x] = 1
    while queue:
        x = queue.popleft()
        for i in friends[x]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                group[0] += 1
                group[1] += candies[i]
    return group


input = sys.stdin.readline
N, M, K = map(int, input().split())
candies = [0]+list(map(int, input().split()))
friends = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
visited = [0]*(N+1)
groups = []
for i in range(1, N+1):
    if not visited[i]:
        groups.append(bfs(i))
l = len(groups)
dp = [[0]*(K+1) for _ in range(l+1)]
for i in range(1, l+1):
    weight, value = groups[i-1][0], groups[i-1][1]
    for j in range(1, K+1):
        if j <= weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-weight]+value, dp[i-1][j])
print(dp[l][K])
