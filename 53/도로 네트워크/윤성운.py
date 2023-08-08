import sys
input = sys.stdin.readline

# 높이 맞추기
def make_same_depth(n1, n2):
    power = 18
    min_cost = 1000000 * 100000 + 1
    max_cost = -1
    while depth[n1] != depth[n2]:
        if depth[n1] - 2 ** power < depth[n2]:
            power -= 1
        else:
            # 해당 조상까지의 최소, 최대 비용 갱신
            min_cost = min(min_cost, parent[power][n1][1])
            max_cost = max(max_cost, parent[power][n1][2])
            n1 = parent[power][n1][0]
    return n1, n2, min_cost, max_cost


N = int(input())
adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    n1, n2, cost = map(int, input().split())
    adj_list[n1].append((n2, cost))
    adj_list[n2].append((n1, cost))

parent = [[(0, 0, 0) for _ in range(N + 1)] for _ in range(18)]
stack = [(1, 0)]
visited = [0] * (N + 1)
depth = [0] * (N + 1)
while stack:
    current = stack.pop()
    if visited[current[0]]:
        continue
    visited[current[0]] = 1
    depth[current[0]] = current[1]
    for destination_info in adj_list[current[0]]:
        if not visited[destination_info[0]]:
            stack.append((destination_info[0], current[1] + 1))
            # 부모까지의 거리 함께 저장
            parent[0][destination_info[0]] = (current[0], destination_info[1], destination_info[1])

# dp
# (j번 노드의 2^i번째 조상, 조상까지 최소 비용, 조상까지 최대 비용)
for i in range(1, 18):
    for j in range(1, N + 1):
        if depth[j] >= 2 ** i:
            parent[i][j] = (parent[i - 1][parent[i - 1][j][0]][0], min(parent[i - 1][j][1], parent[i - 1][parent[i - 1][j][0]][1]), max(parent[i - 1][j][2], parent[i - 1][parent[i - 1][j][0]][2]))

# LCA
K = int(input())
for _ in range(K):
    n1, n2 = map(int, input().split())
    if n1 == n2:
        print(0, 0)
        continue

    # 높이 맞추기
    # 노드 10만: 최대 깊이 < 2^18
    power = 18
    if depth[n1] > depth[n2]:
        n1, n2, min_cost, max_cost = make_same_depth(n1, n2)
    else:
        n1, n2, min_cost, max_cost = make_same_depth(n2, n1)
    if n1 == n2:
        print(min_cost, max_cost)
        continue

    # 최소 공통 조상 찾기
    power = 18
    while power > -1:
        if depth[n1] - 2 ** power >= 0 and parent[power][n1][0] != parent[power][n2][0]:
            # 해당 조상까지의 최소, 최대 비용 갱신
            min_cost = min(min_cost, parent[power][n1][1], parent[power][n2][1])
            max_cost = max(max_cost, parent[power][n1][2], parent[power][n2][2])
            n1 = parent[power][n1][0]
            n2 = parent[power][n2][0]
        power -= 1

    # 마지막으로 부모로 가는 비용도 확인
    min_cost = min(min_cost, parent[0][n1][1], parent[0][n2][1])
    max_cost = max(max_cost, parent[0][n1][2], parent[0][n2][2])
    print(min_cost, max_cost)
    