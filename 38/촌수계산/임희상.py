from collections import deque
N = int(input())
a, b = map(int, input().split())
adj = [[] for _ in range(N+1)]

E = int(input())
for _ in range(E):
  parent, child = map(int, input().split())
  adj[parent].append(child)
  adj[child].append(parent)


queue = deque([(a, 0)])
visited = set()
dists = [-1] * (N+1)

while queue:
  current, dist = queue.popleft()
  if current in visited:
    continue
  visited.add(current)
  dists[current] = dist
  for destination in adj[current]:
    if destination not in visited:
      queue.append((destination, dist+1))
print(dists[b])

