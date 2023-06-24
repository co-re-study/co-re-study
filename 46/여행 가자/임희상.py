N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j]:
            adj[i+1].append(j+1)


plan = list(map(int, input().split()))

stack = [plan[0]]

visited = set()
while stack:
    current = stack.pop()
    if current in visited:
        continue
    visited.add(current)
    for destination in adj[current]:
        if destination not in visited:
            stack.append(destination)

for node in plan:
    if node not in visited:
        print('NO')
        break
else:
    print('YES')
