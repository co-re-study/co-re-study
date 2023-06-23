import sys, math
input = sys.stdin.readline

N = int(input())
adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

# 부모 노드부터 찾기
parent = [0] * (N + 1)
stack = [(1, 0)]
max_depth = 0
depth_dict = dict()
while stack:
    current, depth = stack.pop()
    depth_dict[current] = depth
    if depth > max_depth:
        max_depth = depth
    for adj_node in adj_list[current]:
        if adj_node not in depth_dict:
            parent[adj_node] = current
            stack.append((adj_node, depth + 1))

# DP로 조상 테이블 만들기
ancestor = [[0] * (N + 1) for _ in range(int(math.log2(max_depth)))]
ancestor.insert(0, parent)
max_power = int(math.log2(max_depth)) # 최대 차수
for i in range(1, max_power + 1):
    for j in range(1, N + 1):
        if ancestor[i - 1][j]:
            ancestor[i][j] = ancestor[i - 1][ancestor[i - 1][j]]

# 가장 가까운 조상 찾기
M = int(input())
for _ in range(M):
    n1, n2 = map(int, input().split())
    deeper_depth, shallower_depth = max(depth_dict[n1], depth_dict[n2]), min(depth_dict[n1], depth_dict[n2])
    deeper_node, shallower_node = (n1, n2) if depth_dict[n1] > depth_dict[n2] else (n2, n1)

    # 높이 맞추기
    for power in range(max_power, -1, -1):
        if deeper_depth - 2 ** power >= shallower_depth:
            deeper_depth -= 2 ** power
            deeper_node = ancestor[power][deeper_node]
    
    if deeper_node == shallower_node:
        print(deeper_node)
        continue

    # 조상 찾기
    current_depth = deeper_depth
    for power in range(max_power, -1, -1):
        if current_depth - 2 ** power <= 0:
            continue
        if ancestor[power][deeper_node] == ancestor[power][shallower_node]:
            continue
        current_depth -= 2 ** power
        deeper_node = ancestor[power][deeper_node]
        shallower_node = ancestor[power][shallower_node]

    print(parent[deeper_node])
