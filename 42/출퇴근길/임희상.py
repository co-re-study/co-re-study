import sys

def dfs(start):
    global scc_stack

n, m = map(int, input().split())
nodes = [0] * (n+1)
adj = [[] for _ in range(n+1)]
reversed_adj = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    adj[start].append(end)
    reversed_adj[end].append(start)

S, T = map(int, input().split())

stack = [S]
visited = set()
while stack:
    current = stack.pop()
    if current in visited or current == T:
        continue
    visited.add(current)
    for destination in adj[current]:
        if destination not in visited:
            stack.append(destination)
s_start = set(visited)


stack = [S]
visited = set()
while stack:
    current = stack.pop()
    if current in visited:
        continue
    visited.add(current)
    for destination in reversed_adj[current]:
        if destination not in visited:
            stack.append(destination)
s_set = s_start.intersection(visited)

stack = [T]
visited = set()
while stack:
    current = stack.pop()
    if current in visited or current == S:
        continue
    visited.add(current)
    for destination in adj[current]:
        if destination not in visited:
            stack.append(destination)
t_start = set(visited)

stack = [T]
visited = set()
while stack:
    current = stack.pop()
    if current in visited:
        continue
    visited.add(current)
    for destination in reversed_adj[current]:
        if destination not in visited:
            stack.append(destination)

t_set = t_start.intersection(visited)

print(len(t_set.intersection(s_set)))