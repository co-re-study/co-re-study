from collections import deque

N, S, D = map(int, input().split())

# 인접 노드 저장
adj_list = [[] for _ in range(N)]
for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    adj_list[n1 - 1].append(n2 - 1)
    adj_list[n2 - 1].append(n1 - 1)

# 트리 만들기
stack = [S - 1]
visited = set()
parent = list(range(N))
children_cnt = [0] * N
queue = deque()
while stack:
    current = stack.pop()
    if current in visited:
        continue
    visited.add(current)
    cnt = 0
    for destination in adj_list[current]:
        if destination not in visited:
            stack.append(destination)
            parent[destination] = current
            children_cnt[current] += 1
    if not children_cnt[current]:
        queue.append((current, 0))

is_path = [False] * N # 경로에 포함되는지 여부
acc = [1] * N # 모든 경로는 1로 시작
acc[S - 1] = 0 # 출발할 때는 답에 포함 x

# 리프 노드부터 루트 노드로
while queue:
    current_node, distance_to_leaf = queue.popleft()
    if current_node == S - 1:
        break
        
    # 현재 노드에서 더 갈 필요가 없으면, 경로에 추가
    if distance_to_leaf == D:
        is_path[current_node] = True
        
    # 현재 노드가 경로에 포함되어 있으면 부모 노드도 경로에 추가
    if is_path[current_node]:
        acc[parent[current_node]] += 1
        is_path[parent[current_node]] = True
        
    # 자식 노드를 다 본 노드는 큐에 추가
    children_cnt[parent[current_node]] -= 1
    if not children_cnt[parent[current_node]]:
        queue.append((parent[current_node], distance_to_leaf + 1))

# 경로에 있으면 누적
answer = 0
for n in range(N):
    if is_path[n]:
        answer += acc[n]
print(answer)