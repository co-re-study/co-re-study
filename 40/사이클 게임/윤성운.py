import sys
input = sys.stdin.readline

def find_parent(node):
    while node != parent[node]:
        node = parent[node]
    return node

def union(node1, node2):
    node1 = find_parent(node1)
    node2 = find_parent(node2)
    if node1 < node2:
        parent[node2] = node1
    else:
        parent[node1] = node2

n, m = map(int, input().split())
parent = list(range(n))

answer = 0
for step in range(1, m + 1):
    node1, node2 = map(int, input().split())

    # 부모 다르면 union
    if find_parent(node1) != find_parent(node2):
        union(node1, node2)
    # 부모 같으면 답 출력
    else:
        answer = step
        break

print(answer)
