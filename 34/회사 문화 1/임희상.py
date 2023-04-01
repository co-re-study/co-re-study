from collections import deque
import sys
n, m = map(int, input().split())
complements = [0] * (n+1)
children = [[] for _ in range(n+1)]

boss_chart = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    children[boss_chart[i]].append(i+1)

for i in range(m):
    target, complement = map(int, sys.stdin.readline().split())
    complements[target] += complement

queue = deque([1])
while queue:
    current = queue.popleft()

    for child in children[current]:
        complements[child] += complements[current]
        queue.append(child)

print(*complements[1:])

