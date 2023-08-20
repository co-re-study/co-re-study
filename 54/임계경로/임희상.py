n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]
parents = [set() for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    adj[start].append([end, cost])
    parents[end].add(start)

start, end = map(int, input().split())

reversed = [[] for _ in range(n+1)]
costs = [0] * (n+1)
stack = [start]


# 재귀구현 시간초과


while stack:
    current = stack.pop()
    cost_sum = costs[current]
    for destination_info in adj[current]:
        destination, cost = destination_info
        if cost_sum + cost > costs[destination]:
            costs[destination] = cost_sum + cost
            reversed[destination] = [current]
        elif cost_sum + cost == costs[destination]:
            reversed[destination].append(current)
    
        parents[destination].discard(current)
        if not parents[destination]:
            stack.append(destination)

answer = 0
stack = [end]
visited = set()

while stack:
    current = stack.pop()
    if current in visited:
        continue
    visited.add(current)
    for destination in reversed[current]:
        answer += 1
        if destination not in visited:
            stack.append(destination)

print(costs[end])
print(answer)