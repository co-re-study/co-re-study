N = int(input())
depth = 0
temp = N
while temp:
    depth += 1
    temp //= 2

adj = [[] for _ in range(N+1)]

for _ in range(N-1):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

ancestors = [[0] * (depth) for _ in range(N+1)]
levels = [0] * (N+1)

stack = [(1, 0)]
visited = set()
while stack:
    current, level = stack.pop()
    if current in visited:
        continue
    levels[current] = level
    visited.add(current)
    
    for destination in adj[current]:
        if destination not in visited:
            ancestors[destination][0] = current
            stack.append((destination, level+1))
    temp = 1
    level //= 2
    while level:
        ancestors[current][temp] = ancestors[ancestors[current][temp-1]][temp-1]
        level //= 2
        temp += 1

M = int(input())
for _ in range(M):
    left, right = map(int, input().split())
    target = left if levels[left] > levels[right] else right
    other = right if levels[left] > levels[right] else left
    diff = abs(levels[target] - levels[other])
    for i in range(depth-1, -1, -1):
        if 2**i <= diff:
            target = ancestors[target][i]
            diff -= 2**i
    if target == other:
        print(target)
        continue
    
    for i in range(depth-1, -1, -1):
        if ancestors[target][i] != ancestors[other][i]:
            target = ancestors[target][i]
            other = ancestors[other][i]
    print(ancestors[target][0])
