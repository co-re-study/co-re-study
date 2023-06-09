import heapq
n, s = map(int, input().split())

m = int(input())
speeds = []

heap = []
for i in range(m):
    speed = int(input())
    speeds.append(speed)
    heapq.heappush(heap, [speed, i])
    n -= 1
    if n == s:
        print(i+1)

while n > s:
    current, member = heapq.heappop(heap)
    n -= 1
    if n == s:
        print(member+1)
        break
    heapq.heappush(heap, [current+speeds[member], member])
