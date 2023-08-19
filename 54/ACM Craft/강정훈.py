# from collections import deque
# T = int(input())
#
# for tc in range(T):
#     N, K = map(int, input().split())
#     building_time_list = [0] + list(map(int, input().split()))
#     down_tech_tree = dict()
#     up_tech_tree = dict()
#     for i in range(K):
#         pre, nxt = map(int, input().split())
#         if nxt not in down_tech_tree:
#             down_tech_tree[nxt] = [pre]
#         else:
#             down_tech_tree[nxt].append(pre)
#         if pre not in up_tech_tree:
#             up_tech_tree[pre] = [nxt]
#         else:
#             up_tech_tree[pre].append(nxt)
#     target = int(input())
#     exact_time_list = [0 for _ in range(N+1)]
#     target_queue = deque([target])
#     leafs = set()
#
#     while target_queue:
#         building_num = target_queue.popleft()
#         if building_num not in down_tech_tree:
#             leafs.add(building_num)
#         else:
#             for i in down_tech_tree[building_num]:
#                 target_queue.append(i)
#     road_list = [999999999 for _ in range(N+1)]
#     for i in range(len(leafs)):
#         building_num = leafs.pop()
#         dfs_queue = deque([(building_num, building_time_list[building_num])])
#         while dfs_queue:
#            current_num, current_time = dfs_queue.pop()
#            if (road_list[current_num] > current_time) and (current_num in up_tech_tree):
#                road_list[current_num] = current_time
#                for nxt_num in up_tech_tree[current_num]:
#                    if nxt_num == target:
#                        continue
#                    dfs_queue.append((nxt_num, current_time + building_time_list[nxt_num]))
#     answer = 0
#     if target in down_tech_tree:
#         for i in down_tech_tree[target]:
#             if answer < road_list[i]:
#                 answer = road_list[i]
#     print(answer + building_time_list[target])

from collections import deque
T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    building_time_list = [0] + list(map(int, input().split()))
    building_relation_to_down_dict = dict()
    building_relation_to_up_dict = dict()
    degree = [0 for _ in range(N + 1)]
    for i in range(K):
        pre, next = map(int, input().split())
        if next not in building_relation_to_down_dict:
            building_relation_to_down_dict[next] = [pre]
        else:
            building_relation_to_down_dict[next].append(pre)
        if pre not in building_relation_to_up_dict:
            building_relation_to_up_dict[pre] = [next]
        else:
            building_relation_to_up_dict[pre].append(next)
        degree[next] += 1

    target_building = int(input())
    leaf_list = deque([])
    for i in range(1, N+1):
        if i not in building_relation_to_down_dict:
            leaf_list.append(i)

    least_building_time = [0 for _ in range(N+1)]
    for i in leaf_list:
        least_building_time[i] = building_time_list[i]

    dfs_queue = deque(leaf_list)

    while dfs_queue:
        current = dfs_queue.popleft()
        if current in building_relation_to_up_dict:
            for i in building_relation_to_up_dict[current]:
                degree[i] -= 1
                least_building_time[i] = max(least_building_time[current] + building_time_list[i], least_building_time[i])
                if degree[i] == 0:
                    dfs_queue.append(i)
    print(least_building_time[target_building])









