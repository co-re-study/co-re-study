from collections import deque

N = int(input())
adj = [[] for _ in range(N+1)]

for _ in range(N-1):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

queue = deque([1])
visited = set()
sequence = list(map(int, input().split()))
idx = 1

while queue:

    current = queue.popleft()
    visited.add(current)
    destinations = set()
    
    for destination in adj[current]:
        if destination not in visited:
            destinations.add(destination)
    
    for _ in range(len(destinations)):
        if sequence[idx] not in destinations:
            print(0)
            exit(0)
        queue.append(sequence[idx])
        idx += 1

print(1)

