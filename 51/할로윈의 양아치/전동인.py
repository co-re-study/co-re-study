def find(x):
    while x != parents[x]:
        x = parents[x]
    return x


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        if size[x] < size[y]:
            x, y = y, x
        parents[y] = x
        size[x] += size[y]


n, m, k = map(int, input().split())
candy = [0] + list(map(int, input().split()))
parents = list(range(n+1))
size = [1] * (n+1)
dp = [0] * k

# 그룹화
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

# 그룹단위 사이즈, 캔디 정리
group_candy = [0] * (n+1)
group_size = [0] * (n+1)
for i in range(1, n+1):
    group = find(i)
    group_candy[group] += candy[i]
    group_size[group] = size[group]

# 0-1 Knapsack
for i in range(1, n+1):
    if parents[i] == i:
        old_dp = dp[:]
        for j in range(group_size[i], k):
            # j는 현재 고려하고 있는 가방 용량
            # 기존과 비교해서 (현재 그룹 캔디 + 남은 용량의 최대 캔디) 중에서 더 큰 값을 고른다.
            dp[j] = max(dp[j], old_dp[j-group_size[i]]+group_candy[i])


print(dp[-1])
