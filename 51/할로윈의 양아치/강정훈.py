def find_root(x):
    if x != root[x]:
        return find_root(root[x])
    else:
        return x


def union(x, y):
    if root[x] == root[y]:
        return
    else:
        x = find_root(x)
        y = find_root(y)
        if rank[x] > rank[y]:
            rank[y] = rank[x]
            root[y] = root[x]
        elif rank[x] == rank[y]:
            rank[x] += 1
            root[y] = x
        else:
            rank[x] = rank[y]
            root[x] = root[y]


N, M, K = map(int, input().split())
candis_num = [0]+list(map(int, input().split()))
root = [i for i in range(N+1)]
rank = [1]*(N+1)
zip_dan = dict()

for i in range(M):
    friend1, friend2 = map(int, input().split())
    if find_root(friend1) != find_root(friend2):
        union(friend1, friend2)

#
visited = set()
for i in range(1, len(root)):
    if root[i] not in visited:
        zip_dan[root[i]] = (candis_num[i], 1)
        visited.add(root[i])
    else:
        zip_dan[root[i]] = (zip_dan[root[i]][0] + candis_num[i], zip_dan[root[i]][1] + 1)
zip_dan_list = []
for i in visited:
    if zip_dan[root[i]][1] < K:
        zip_dan_list.append(zip_dan[root[i]])
zip_dan_list.sort(key=lambda x: (-x[0], x[1]))
dp = [[(0, 0) for _ in range(len(zip_dan_list)+1)] for _ in range(len(zip_dan_list)+1)]
dp[0] = [(0, 0)] + zip_dan_list[:]
for i in range(1, len(dp)):
    for j in range(1, len(dp)):
        if i == j:
            dp[i][j] = dp[i-1][j]
            continue
        if (dp[i-1][i][1] + dp[i-1][j][1]) < K:
            dp[i][j] = (dp[i-1][i][0] + dp[i-1][j][0], dp[i-1][i][1] + dp[i-1][j][1])
        else:
            dp[i][j] = dp[i-1][j]

answer = 0
for i in range(len(dp)):
    if answer < dp[-1][i][0]:
        answer = dp[-1][i][0]
print(zip_dan_list)
print(dp)
print(answer)

