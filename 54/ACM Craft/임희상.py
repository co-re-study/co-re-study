import heapq

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    build_times = [0] + list(map(int, input().split()))
    required = {}
    children = [[] for _ in range(N+1)]
    for i in range(K):
        parent, child = map(int, input().split())
        children[parent].append(child)
        if child in required.keys():
            required[child].add(parent)
        else:
            required[child] = {parent}

    heap = []
    visited = set()
    for i in range(1, N+1):
        if i not in required.keys():
            heapq.heappush(heap, (build_times[i], i))
    
    target = int(input())
    while heap:
        now, current = heapq.heappop(heap)
        if current == target:
            print(now)
            break
        for destination in children[current]:
            required[destination].discard(current)
            if not required[destination]:
                heapq.heappush(heap, (now + build_times[destination], destination))

    