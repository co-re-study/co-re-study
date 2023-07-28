N, M, K = map(int, input().split())

candies = list(map(int, input().split()))
parents = list(range(N+1))


def union(x, y):
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]



for _ in range(M):
    one, other = map(int, input().split())
    one = find(one)
    other = find(other)
    if one != other:
        union(one, other)

for i in range(1, N+1):
    find(i)


groups = {}
for i in range(1, N+1):
    if parents[i] in groups.keys():
        groups[parents[i]][0] += 1
        groups[parents[i]][1] += candies[i-1]
    else:
        groups[parents[i]] = [1, candies[i-1]]
    
    
dp = [[0] * (K+1) for _ in range(len(groups)+1)]
group_idx = 1
for head in groups.keys():
    children_count, candies_count = groups[head]
    for k in range(1, K+1):
        if children_count >= k:
            dp[group_idx][k] = dp[group_idx-1][k]
        else:
            dp[group_idx][k] = max(dp[group_idx-1][k-children_count] + candies_count, dp[group_idx-1][k])
    
    group_idx += 1

print(dp[group_idx-1][K])
