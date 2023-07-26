import sys
input = sys.stdin.readline

def find_parent(n):
    if parent[n] != n:
        parent[n] = find_parent(parent[n])
    return parent[n]


def union(n1, n2):
    if n1 < n2:
        parent[n2] = n1
    else:
        parent[n1] = n2


N, M, K = map(int, input().split())
candies = list(map(int, input().split()))
parent = list(range(N))

# union-find
for _ in range(M):
    n1, n2 = map(lambda x: int(x) - 1, input().split())
    n1 = find_parent(n1)
    n2 = find_parent(n2)
    if n1 != n2:
        union(n1, n2)

for i in range(N):
    find_parent(i)

# key: 부모 번호, value: [연결된 노드 수, 사탕의 합]
# ex) {0: [2, 13], 1: [4, 26], 3: [2, 24], 6: [2, 33]}
parent_dict = dict()
for i in range(N):
    if parent[i] in parent_dict:
        parent_dict[parent[i]][0] += 1
        parent_dict[parent[i]][1] += candies[i]
    else:
        parent_dict[i] = [1, candies[i]]

# 딕셔너리를 리스트로 변환
# ex) [[2, 13], [4, 26], [2, 24], [2, 33]]
friend_info = [i for i in parent_dict.values()]

# 1차원 dp
dp = [0] * K
for i in range(len(friend_info)):
    for j in range(K - 1, 0, -1):
        if j >= friend_info[i][0]:
            dp[j] = max(friend_info[i][1] + dp[j - friend_info[i][0]], dp[j])

print(dp[-1])