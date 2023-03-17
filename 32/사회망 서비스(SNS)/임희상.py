from collections import deque

N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)
parents = [0] * (N+1)
children = [[] for _ in range(N+1)]
children_cnt = [0] * (N+1)
stack = [1]
visited = set()
queue = deque([])
while stack:
    current = stack.pop()
    if current in visited:
        continue
    visited.add(current)
    for destination in adj[current]:
        if destination not in visited:
            stack.append(destination)
            parents[destination] = current
            children[current].append(destination)
            children_cnt[current] += 1
    if not children[current]:
        queue.append(current)
answers = [[1, 0] for _ in range(N+1)]  # [감, 안감]
while queue:
    current = queue.popleft()
    for child in children[current]:
        answers[current][0] += min(answers[child])
        answers[current][1] += answers[child][0]
    children_cnt[parents[current]] -= 1
    if not children_cnt[parents[current]]:
        queue.append(parents[current])
print(min(answers[1]))


