N, M, K = map(int, input().split())
candy = list(map(int, input().split()))


def find(n):
    if tree[n] == n:
        return n
    else:
        tree[n] = find(tree[n])
        return tree[n]
    
tree = list(range(N))
if M:
    for a, b in list(tuple(map(lambda x: int(x) - 1, input().split())) for m in range(M)):
        a, b = find(a), find(b)
        tree[max(a, b)] = min(a, b)

group = {}
for t in range(N):
    root = find(tree[t])
    if root not in group:
        group[root] = [1, candy[t]]
    else:
        group[root][0] += 1
        group[root][1] += candy[t]

dp = [0] * K
roots = list(group.keys())
for i in range(len(roots)):
    for j in range(K - 1, -1, -1):
        if group[roots[i]][0] <= j:
            dp[j] = max(dp[j], group[roots[i]][1] + dp[j - group[roots[i]][0]])
print(dp[-1])