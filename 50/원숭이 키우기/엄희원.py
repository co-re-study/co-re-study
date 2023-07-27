###### 모르겟당 다시 풀기


# from collections import deque
# N = int(input())
#
# arr = list(map(int, input().split()))
#
# power = list(map(int, input().split()))
#
# D = int(input())
#
# info = {}
# for i in range(len(arr)):
#     info[i+1] = deque([i+1] * arr[i])
#
# power_info = []
# for i in range(len(power)):
#     power_info.append([power[i], i+1])
# power_info.sort(reverse=True)
#
# # print(info)
# print(power_info)
# visited = set()
# for p in power_info:
#     visited.add(p[1])
#     if D == 0:
#         break
#     k = 1
#     while True:
#         if p[1] - k > 0 and D != 0 and p[1] - k not in visited:
#            while info[p[1] - k]:
#                ch = info[p[1] - k].popleft()
#                if p[1] - ch <= D:
#                    D -= (p[1] - ch)
#                    ch = p[1]
#                    info[p[1]].append(ch)
#                else:
#                    info[p[1] - k].append(ch)
#                    break
#         k += 1
#         if p[1] - k <= 0 or p[1] - k in visited or D == 0:
#             break
#
# print(info)
# ans = 0
# for p in power_info:
#     ans += p[0] * len(info[p[1]])
# print(ans)






