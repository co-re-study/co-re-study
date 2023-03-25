from collections import deque
N, S, D = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

stack = [[S, 0]]
dists = [0] * (N+1)
parents = [0] * (N+1)
children = [[] for _ in range(N+1)]
visited = set()
required = set()
while stack:
    current, dist = stack.pop()
    if current in visited:
        continue
    visited.add(current)
    for destination in adj[current]:
        if destination not in visited:
            stack.append([destination, dist+1])
            parents[destination] = current
            children[current].append(destination)
    if not children[current]:
        str = D
        while str:
            current = parents[current]
            if current in required:
                break
            str -= 1
        required.add(current)

queue = deque(list(required))
visited = set()
while queue:
    current = queue.popleft()
    if not current or current == S:
        continue
    if current in visited:
        continue
    visited.add(current)
    if parents[current] in visited:
        dists[S] += dists[current] + 2
        continue
    dists[parents[current]] += dists[current] + 2
    queue.append(parents[current])

print(dists[S])


