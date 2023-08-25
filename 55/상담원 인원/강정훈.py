'''
동시성이 성립하지 않는데, 동시성이 성립되는 로직 작성함. 흑흑 다시짜야함.1번 케이스는 통과하는데, 2번 케이스가 통과가 안됨..
'''
#
# def solution(k, n, reqs):
#     answer = 1e9
#     consulting_time_list = [[0 for _ in range(171)] for _ in range(k + 1)]
#     max_consulting_time = 0
#     for start, time, consult_type in reqs:
#         consulting_time_list[consult_type][start] += 1
#         consulting_time_list[consult_type][start + time] -= 1
#         if start + time > max_consulting_time:
#             max_consulting_time = start + time
#     for i in range(1, k+1):
#         for j in range(1, max_consulting_time+1):
#             consulting_time_list[i][j] += consulting_time_list[i][j-1]
#
#     mento_num = k
#     mento_num_list = [0] + [1 for _ in range(k)]
#     while mento_num <= n:
#         waiting_time_list = [0 for _ in range(k + 1)]
#         for i in range(1, k+1):
#             for j in range(1, max_consulting_time+1):
#                 if consulting_time_list[i][j] > mento_num_list[i]:
#                     waiting_time_list[i] += (consulting_time_list[i][j] - mento_num_list[i])
#         max_wating_time = (0, 0)
#         for i in range(1, k+1):
#             if max_wating_time[1] < waiting_time_list[i]:
#                 max_wating_time = (i, waiting_time_list[i])
#         mento_num_list[max_wating_time[0]] += 1
#         print(waiting_time_list)
#         answer = sum(waiting_time_list)
#         mento_num += 1
#
#
#     return answer
#
# print(solution(3, 5, [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]))
# print(solution(2, 3, [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]))

