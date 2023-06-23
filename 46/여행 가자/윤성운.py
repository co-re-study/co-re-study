import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(N)]
route = list(map(lambda x: int(x) - 1, input().split()))

# DFS
stack = [route[0]]
visited = [0] * N
while stack:
    current = stack.pop()
    if visited[current]:
        continue
    visited[current] = 1
    for adj_node in range(N):
        if adj_matrix[current][adj_node] and not visited[adj_node]:
            stack.append(adj_node)

# 루트 중 visited에 속하지 않은 노드가 있다면 NO 출력
for node in route:
    if not visited[node]:
        print("NO")
        break
else:
    print("YES")
            