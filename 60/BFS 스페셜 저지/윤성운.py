import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

order = list(map(int, input().split()))
queue = deque([1])
visited = [0] * (N + 1)
visited[1] = 1
idx = 1

while queue:
    current = queue.popleft()
    adj_nodes = set()
    for dest in adj_list[current]:
        if not visited[dest]:
            visited[dest] = 1
            adj_nodes.add(dest)
    for _ in range(len(adj_nodes)):
        if order[idx] in adj_nodes:
            queue.append(order[idx])
        else:
            print(0)
            exit(0)
        idx += 1

print(1)