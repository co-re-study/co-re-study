import sys, heapq
input = sys.stdin.readline

n = int(input())
distances = []
for _ in range(n):
    home, office = map(int, input().split())
    distances.append((min(home, office), max(home, office)))
distances.sort(key=lambda x: (x[1], x[0])) # 큰 값 기준 오름차순 정렬

d = int(input())
answer = 0
window = []
for start, end in distances:
    if end - start > d:
        continue
    while window and window[0] + d < end:
        heapq.heappop(window)
    heapq.heappush(window, start) # 작은 값 우선순위 큐
    answer = max(answer, len(window))

print(answer)