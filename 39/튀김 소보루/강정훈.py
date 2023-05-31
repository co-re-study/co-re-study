import sys
from heapq import heappop, heappush

# N, S = map(int, sys.stdin.readline().split())
# m = int(input())
# personal_time = [0] + [int(sys.stdin.readline()) for _ in range(m)]
#
# time = 0
# last_person = 0
# queue = deque()
# for i in range(1, m+1):
#     queue.append(i)
# flag = False
# while N > S:
#     for i in range(len(queue)):
#         last_person = queue.popleft()
#         N -= 1
#         if N == S:
#             flag = True
#             break
#     if flag:
#         break
#     if time == 0:
#         time += 1
#         continue
#     for i in range(1, m+1):
#         if time % personal_time[i] == 0:
#             queue.append(i)
#     time += 1
#
# print(last_person)

N, S = map(int, sys.stdin.readline().split())
m = int(input())
personal_time = [0] + [int(sys.stdin.readline()) for _ in range(m)]


heap = []
for i in range(1, m+1):
    heappush(heap, (0, i))

while N > S:
    time, person = heappop(heap)
    N -= 1
    if N == S:
        print(person)
        break
    heappush(heap, (time+personal_time[person], person))

