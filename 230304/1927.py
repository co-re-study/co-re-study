from heapq import heappush, heappop
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

heap = []
n = int(input())

for _ in range(n):
    num = int(input())
    if num:
        heappush(heap, num)
    else:
        if len(heap):
            print(heappop(heap))
        else:
            print(0)