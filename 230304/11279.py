import sys, heapq
input = lambda : sys.stdin.readline().rstrip('\r\n')

n = int(input())
max_heap = []

for num in list(int(input()) for _ in range(n)):
    if num:
        heapq.heappush(max_heap, (-num, num))       # 최대 힙은 튜플의 첫번째 자리에 음수로 만들어 넣으면 최소값 순으로 정렬됨 
    else:
        if max_heap:
            print(heapq.heappop(max_heap)[1])       # 최소 튜플의 두번째 자리 값이 최대 값이됨
        else:
            print(0)