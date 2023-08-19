# from collections import deque
# import sys
# input=sys.stdin.readline
#
# flag = True
# while flag:
#     N = int(input())
#     if N == 0:
#         flag = False
#         break
#     room_info_dict = dict()
#     for i in range(1, N+1):
#         information = input().split()
#         room_info_dict[i] = information
#     answer = False
#     room_road_deque = deque([["1"] + ["0"] + room_info_dict[1]])
#     while room_road_deque:
#         visited = set()
#         current = room_road_deque.popleft()
#         current_room, current_money, kind, cost, roads \
#             = int(current[0]), int(current[1]), current[2], int(current[3]), current[4:-1]
#         visited.add((current_room, current_money))
#         if kind == 'T':
#             if current_money >= cost:
#                 current_money -= cost
#             else:
#                 continue
#         elif kind == 'L':
#             if current_money < cost:
#                 current_money = cost
#         if current_room == N:
#             answer = True
#             break
#         for i in roads:
#             i = int(i)
#             if (i, current_money) in visited:
#                 continue
#             room_road_deque.append([str(i)] + [str(current_money)] + room_info_dict[i])
#     if answer:
#         print("Yes")
#     else:
#         print("No")


# from collections import deque
# import sys
# input=sys.stdin.readline
#
# flag = True
# while flag:
#     N = int(input())
#     if N == 0:
#         flag = False
#         break
#     room_info_dict = dict()
#     for i in range(1, N+1):
#         information = input().split()
#         room_info_dict[i] = ['0'] + information
#     answer = False
#     room_road_deque = deque([["1"] + ["0"] + room_info_dict[1]])
#     visited = set()
#     while room_road_deque:
#         current = room_road_deque.popleft()
#         current_room, current_money, max_money, kind, cost, roads \
#             = int(current[0]), int(current[1]), int(current[2]), current[3], int(current[4]), current[5:-1]
#         visited.add((current_room, current_money))
#         if kind == 'T':
#             if current_money >= cost:
#                 current_money -= cost
#             else:
#                 continue
#         elif kind == 'L':
#             if current_money < cost:
#                 current_money = cost
#         if current_room == N:
#             answer = True
#             break
#         for i in roads:
#             i = int(i)
#             if (i, current_money) in visited:
#                 continue
#             if current_money >= int(room_info_dict[i][0]):
#                 room_info_dict[i][0] = str(current_money)
#             else:
#                 continue
#             room_road_deque.append([str(i)] + [str(current_money)] + room_info_dict[i])
#     if answer:
#         print("Yes")
#     else:
#         print("No")

'''
2차시도까지는 visited를 set으로 써서 방번호와 현재 갖고 있는 돈을 넣었다.
이번 시도에서는 특정 방을 방문했을 때 당시 가장 많이 갖고 있던 돈과 현재 갖고 있던 돈을 범위로 비교했다.
-> 불필요한 deque로의 삽입을 방지하여 통과했다.
'''

from collections import deque
import sys
input=sys.stdin.readline

flag = True
while flag:
    N = int(input())
    if N == 0:
        flag = False
        break
    room_info_dict = dict()
    for i in range(1, N+1):
        information = input().split()
        room_info_dict[i] = information
    answer = False
    room_road_deque = deque([["1"] + ["0"] + room_info_dict[1]])
    visited = [0 for _ in range(N+1)]
    max_money_list = [0 for _ in range(N+1)]
    while room_road_deque:
        current = room_road_deque.popleft()
        current_room, current_money, kind, cost, roads \
            = int(current[0]), int(current[1]),  current[2], int(current[3]), current[4:-1]
        if kind == 'T':
            if current_money >= cost:
                current_money -= cost
            else:
                continue
        elif kind == 'L':
            if current_money < cost:
                current_money = cost
        if current_room == N:
            answer = True
            break
        visited[current_room] = 1
        if current_money > max_money_list[current_room]:
            max_money_list[current_room] = current_money
        for i in roads:
            i = int(i)
            # 개선한 부분 
            if visited[i] and (max_money_list[i] >= current_money):
                continue
            room_road_deque.append([str(i)] + [str(current_money)] + room_info_dict[i])
    if answer:
        print("Yes")
    else:
        print("No")
