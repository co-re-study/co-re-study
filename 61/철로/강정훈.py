import heapq
import sys
input=sys.stdin.readline
N = int(input())
people_list = []

for i in range(N):
    start, end = map(int, input().split())
    if start > end:
        start, end = end, start
    people_list.append([start, end])
d = int(input())
people_list.sort(key=lambda x: x[1])

answer = 0
q = []

for people in people_list:
    start, end = people
    if end - start > d:
        continue
    if not q:
        q.append(people)
    else:
        while q and q[0][0] < end - d:
            heapq.heappop(q)
        heapq.heappush(q, people)
    answer = max(answer, len(q))

print(answer)






