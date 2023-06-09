import sys
# from collections import deque
#
# N, M = map(int, sys.stdin.readline().split())
#
# relation = [[] for _ in range(N+1)]
# for i in range(M):
#     x, y = map(int, sys.stdin.readline().split())
#     relation[x].append(y)
#     relation[y].append(x)
#
# visited = set()
# odd_check = set()
# even_check = set()
# queue = deque()
# queue.append(x)
# odd_check.add(x)
# flag = False
# while queue:
#     current = queue.popleft()
#     visited.add(current)
#     for i in relation[current]:
#         if i not in visited:
#             if current in odd_check:
#                 even_check.add(i)
#             else:
#                 odd_check.add(i)
#             queue.append(i)
#         elif i in visited:
#             if current in odd_check and (i in odd_check):
#                 flag = True
#                 break
#             elif current in even_check and (i in even_check):
#                 flag = True
#                 break
#     if flag:
#         break
#
# if flag:
#     print(0)
#
# if not flag:
#     print(1)


def find(x):
    if root[x] == x:
        return x
    else:
        return find(root[x])


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] > rank[y]:
        root[y] = x

    elif rank[x] < rank[y]:
        root[x] = y
    else:
        root[y] = x
        rank[x] = rank[x]+1


N, M = map(int, sys.stdin.readline().split())
root = [i for i in range(N+1)]
rank = [0 for _ in range(N+1)]
enemies = [[] for _ in range(N+1)]
flag = False
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    x_root, y_root = find(x), find(y)
    if enemies[x]:
        union(enemies[x][0], y)
    if enemies[y]:
        union(x, enemies[y][0])
    if x_root == y_root:
        flag = True
        break
    enemies[x].append(y)
    enemies[y].append(x)


if flag:
    print(0)
if not flag:
    print(1)
