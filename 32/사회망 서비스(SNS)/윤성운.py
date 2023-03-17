from collections import deque

N = int(input())

adj_list = [[] for _ in range(N)]
for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    adj_list[n1 - 1].append(n2 - 1)
    adj_list[n2 - 1].append(n1 - 1)

parent = [0] * N
stack = [0]
visited = set()
child_cnt = [0] * N
leaves = set()
queue = deque()

# 트리 만들기
while stack:
    current = stack.pop()
    if current in visited:
        continue
    visited.add(current)
    for destination in adj_list[current]:
        if destination not in visited:
            parent[destination] = current
            stack.append(destination)
            child_cnt[current] += 1 # 자식 수 세기
    if not child_cnt[current]:
        leaves.add(current) # 리프 노드 메모
        queue.append(current) # 큐에도 넣어 놓기

# 얼리어답터 노드들
early_nodes = set()

# 리프노드부터 위로 올라가기
while queue:
    current = queue.popleft()

    # 현재 노드가 얼리어답터가 아니면 내 부모 노드는 무조건 얼리어답터로
    if current not in early_nodes:
        early_nodes.add(parent[current])

    # 자식 노드를 모두 봤다면 queue에 추가
    child_cnt[parent[current]] -= 1
    if not child_cnt[parent[current]]:
        if parent[current] == 0:
            continue
        queue.append(parent[current])

print(len(early_nodes))
