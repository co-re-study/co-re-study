# 현재 인덱스 기준, 오른쪽 숫자들로 이루어진 최소힙을 만든다.
# 현재 숫자보다 높은 숫자가 나올 때까지 힙에서 숫자를 꺼낸다.
# 1. 나보다 큰 숫자가 나온 경우: answer의 왼쪽으로 해당 숫자 넣기
# 2. 다 꺼냈는데도 현재 숫자보다 큰 숫자가 없는 경우: answer의 왼쪽으로 -1 넣기

import sys
import heapq
from collections import deque

N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))

answer = deque([-1])
queue = [num_list[-1]]
for num in num_list[-2::-1]:
    while queue:
        # 나보다 큰 숫자가 나왔다면, answer에 넣기
        if num < queue[0]:
            answer.appendleft(queue[0])
            break
        # 아니라면 꺼내기
        else:
            heapq.heappop(queue)
    # 다 꺼냈는데도 나보다 큰 숫자가 없다면 -1 넣기
    else:
        answer.appendleft(-1)
    # 현재 숫자도 힙에 넣기
    heapq.heappush(queue, num)

print(" ".join(map(str, answer)))
