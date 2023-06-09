from collections import deque
from itertools import combinations
# N = int(input())
# friends_dict = dict()
# for i in range(N-1):
#     u, v = map(int, input().split())
#     if not u in friends_dict:
#         friends_dict[u] = [v]
#     else:
#         friends_dict[u].append(v)
#     if not v in friends_dict:
#         friends_dict[v] = [u]
#     else:
#         friends_dict[v].append(u)
# print(friends_dict)
#
# cnt = 0
# arr = range(1, N+1)
# arr_set = set(arr)
# total_flag = False
# for i in range(1, N+1):
#     combi = list(combinations(arr, i))
#     for earlys in combi:
#         visited = set()
#         flag = False
#         for j in range(1, N+1):
#             if j not in earlys:
#                 for k in friends_dict[j]:
#                     if k not in earlys:
#                         flag = True
#                         break
#             if flag:
#                 break
#         if not flag:
#             cnt = i
#             break
#     if not flag:
#         break
# print(cnt)


N = int(input())
parents_dict = dict()
childs_dict = dict()
no_child_list = []
for i in range(N-1):
    u, v = map(int, input().split())
    if not u in parents_dict:
        parents_dict[u] = [v]
    else:
        parents_dict[u].append(v)
    if not v in childs_dict:
        childs_dict[v] = [u]
    else:
        childs_dict[v].append(u)

for i in range(1, N+1):
    if i not in parents_dict:
        no_child_list.append(i)
if 1 in no_child_list:
    parents_dict, childs_dict = childs_dict, parents_dict
    no_child_list = []
    for i in range(1, N + 1):
        if i not in parents_dict:

            no_child_list.append(i)
trees = deque(no_child_list)
Earlys = set()
visited = set()
while trees:
    child = trees.popleft()
    parent = childs_dict[child][0]
    if parent not in visited and parent != 1:
        visited.add(parent)
        trees.append(parent)
    if child not in Earlys:
        Earlys.add(parent)


print(len(Earlys))









