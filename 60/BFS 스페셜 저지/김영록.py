# pypy 2716ms
# from collections import deque
# import sys
# input = sys.stdin.readline
# N = int(input())
# route = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     x, y = map(int, input().split())
#     route[x].append(y)
#     route[y].append(x)
# order = list(map(int, input().split()))
# visited = [0]*(N+1)
# queue = deque([1])
# visited[1] = 1
# idx = 1
# while queue:
#     current = queue.popleft()
#     target = []
#     for destination in route[current]:
#         if not visited[destination]:
#             visited[destination] = 1
#             target.append(destination)
#     for _ in range(len(target)):
#         if order[idx] in target:
#             queue.append(order[idx])
#         else:
#             print(0)
#             exit()
#         idx += 1
# print(1)

from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
route = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    route[x].append(y)
    route[y].append(x)
order = list(map(int, input().split()))
visited = [0]*(N+1)
queue = deque([1])
visited[1] = 1
idx = 1
while queue:
    current = queue.popleft()
    target = []
    for destination in route[current]:
        if not visited[destination]:
            visited[destination] = 1
            target.append(destination)
    if sorted(order[idx:idx+len(target)]) == sorted(target):
        for child in order[idx:idx+len(target)]:
            queue.append(child)
        idx += len(target)
    else:
        print(0)
        exit()
print(1)
